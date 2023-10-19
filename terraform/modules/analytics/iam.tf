resource "google_service_account" "bigquery_user" {
  account_id   = "analytics-user"
  display_name = "BigQuery Service Account"
}

resource "google_project_iam_binding" "bigquery_user_binding_data_editor" {
  project = var.gcp_project
  role    = "roles/bigquery.dataEditor"

  members = [
    "serviceAccount:${google_service_account.bigquery_user.email}",
  ]
}

resource "google_project_iam_binding" "bigquery_user_binding_user" {
  project = var.gcp_project
  role    = "roles/bigquery.user"

  members = [
    "serviceAccount:${google_service_account.bigquery_user.email}",
  ]
}

resource "google_bigquery_dataset_iam_binding" "dataset_permission" {
  dataset_id = google_bigquery_dataset.analytics.dataset_id
  role       = "roles/bigquery.dataEditor"

  members = [
    "serviceAccount:${google_service_account.bigquery_user.email}",
  ]
}
