resource "google_cloud_run_service" "analytics" {
  name     = "cloudrun-srv"
  location = "us-central1"

  template {
    spec {
      containers {
        image = "us-central1-docker.pkg.dev/hummy-app/analytics/api:latest"
        ports {
            container_port = 8000
        }
        liveness_probe {
          http_get {
            path = "/healthz"
          }
        }
        env {
            name = "GCP_PROJECT_ID"
            value = "hummy-app"
        }
      }
      service_account_name = google_service_account.bigquery_user.email
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}

resource "google_cloud_run_service_iam_binding" "public_invoker" {
  service  = google_cloud_run_service.analytics.name
  location = google_cloud_run_service.analytics.location
  role     = "roles/run.invoker"
  members  = ["allUsers"]
}
