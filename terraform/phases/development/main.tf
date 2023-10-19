provider "google" {
  project     = "hummy-app"
  region      = "us-central1"
}

module "analytics" {
  source      = "../../modules/analytics"
  environment = "environment"
  dataset     = "analytics"
  gcp_project = "hummy-app"
}
