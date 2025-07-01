import os
import ember

def main():
    # Specify your dataset directory
    data_dir = "features_families_ember_load/Agensla"

    # Create vectorized features and metadata
    ember.create_vectorized_features(data_dir)
    _ = ember.create_metadata(data_dir)

    # Load metadata and vectorized features
    emberdf = ember.read_metadata(data_dir)
    X_train, y_train, X_test, y_test = ember.read_vectorized_features(data_dir)

    print("Dataset loaded successfully!")
    print(f"- Training set size: {X_train.shape}")
    print(f"- Test set size: {X_test.shape}")
    print(f"- Labels distribution in train: clean={(y_train==0).sum()}, malware={(y_train==1).sum()}")
    print(f"- Labels distribution in test: clean={(y_test==0).sum()}, malware={(y_test==1).sum()}")

if __name__ == "__main__":
    main()
