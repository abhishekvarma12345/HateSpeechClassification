from hate.configuration.gcloud_syncer import GCloudSync

cloud_ops = GCloudSync()

cloud_ops.sync_folder_from_gcloud("hate-speech-classify", "dataset.zip", "cloud_data")