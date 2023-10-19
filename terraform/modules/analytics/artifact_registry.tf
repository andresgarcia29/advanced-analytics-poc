resource "google_artifact_registry_repository" "analytics" {
  location      = "us-central1"
  repository_id = "analytics"
  description   = "analytics docker repository"
  format        = "DOCKER"
}
