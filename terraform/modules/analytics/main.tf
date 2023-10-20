resource "google_bigquery_dataset" "analytics" {
  dataset_id                  = var.dataset
  friendly_name               = var.dataset
  description                 = "This is a ${var.dataset} dataset."
  location                    = "EU"
  default_table_expiration_ms = 3600000000

  labels = {
    env = var.environment
  }
}

resource "google_bigquery_table" "analytics" {
  dataset_id = google_bigquery_dataset.analytics.dataset_id
  table_id   = "products"

  time_partitioning {
    type = "DAY"
  }

  labels = {
    env = var.environment
  }

  schema = <<EOF
[
  {
    "name": "name",
    "type": "STRING",
    "mode": "REQUIRED",
    "description": "The name of the product"
  },
  {
    "name": "cost",
    "type": "INTEGER",
    "mode": "REQUIRED",
    "description": "The cost of the product"
  },
  {
    "name": "description",
    "type": "STRING",
    "mode": "NULLABLE",
    "description": "The description of the product"
  }
]
EOF
}

