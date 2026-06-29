import os 
import pickle 
import pandas as pd
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACTS_DIR = os.path.join(PROJECT_ROOT, "artifacts")
FEATURE_NAMES_PATH = os.path.join( ARTIFACTS_DIR, "feature_names.pkl" )
OHE_ENCODER_PATH = os.path.join( ARTIFACTS_DIR, "ohe_encoder.pkl" )
ORDINAL_MAPPINGS_PATH = os.path.join( ARTIFACTS_DIR, "ordinal_mappings.pkl" )
NOMINAL_FEATURES = [ "Month", "DayOfWeek", "Make", "AccidentArea", "DayOfWeekClaimed", "MonthClaimed", "Sex", "MaritalStatus", "Fault", "VehicleCategory", "PoliceReportFiled", "WitnessPresent", "AgentType", "BasePolicy"]
def load_artifacts():
    with open(FEATURE_NAMES_PATH, "rb") as f:
        feature_names = pickle.load(f)

    with open(OHE_ENCODER_PATH, "rb") as f:
        ohe_encoder = pickle.load(f)

    with open(ORDINAL_MAPPINGS_PATH, "rb") as f:
        ordinal_mappings = pickle.load(f)

    return (
        feature_names,
        ohe_encoder,
        ordinal_mappings
    )
def preprocess_claims(df):
    df = df.copy()

    (
        feature_names,
        ohe_encoder,
        ordinal_mappings
    ) = load_artifacts()

    columns_to_drop = [
        "FraudFound_P",
        "PolicyNumber",
        "RepNumber"
    ]

    existing_columns = [
        col for col in columns_to_drop
        if col in df.columns
    ]

    df.drop(
        columns=existing_columns,
        inplace=True
    )

    if "Age" in df.columns:

        df["Age_Invalid"] = (
            df["Age"] <= 0
        ).astype(int)

        median_age = df.loc[
            df["Age"] > 0,
            "Age"
        ].median()

        df["Age"] = df["Age"].replace(
            0,
            median_age
        )

    for column, mapping in ordinal_mappings.items():

        if column in df.columns:

            df[column] = (
                df[column]
                .astype(str)
                .str.strip()
                .map(mapping)
            )

    ohe_array = ohe_encoder.transform(
        df[NOMINAL_FEATURES]
    )

    ohe_columns = (
        ohe_encoder.get_feature_names_out(
            NOMINAL_FEATURES
        )
    )

    ohe_df = pd.DataFrame(
        ohe_array,
        columns=ohe_columns,
        index=df.index
    )

    df.drop(
        columns=NOMINAL_FEATURES,
        inplace=True
    )

    final_df = pd.concat(
        [df, ohe_df],
        axis=1
    )

    final_df = final_df.reindex(
        columns=feature_names,
        fill_value=0
    )

    return final_df