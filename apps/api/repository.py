import logging
from typing import List

from google.cloud import bigquery
from google.api_core.exceptions import BadRequest, Forbidden

from entities import ProductOut
from core import ProductsFilter

logger = logging.getLogger("app")


class Repository:
    def __init__(self) -> None:
        self.client = self.__create_connection()

    def get_products(self, filters: ProductsFilter) -> List[ProductOut]:
        QUERY = self.__get_products_query_builder(filters=filters)
        logger.info("Query to applied: " + QUERY)
        try:
            query_job = self.client.query(QUERY)
            rows = query_job.result()
            return [ProductOut(**row) for row in rows]
        except BadRequest as error:
            logger.error(error)
        except Forbidden as error:
            logger.error(error)
        return []

    def __get_products_query_builder(self, filters: ProductsFilter) -> str:
        QUERY = "SELECT name, cost, description FROM `hummy-app.analytics.products`"
        if filters.greater:
            QUERY += f" WHERE cost > {filters.costs};"
        if filters.less:
            QUERY += f" WHERE cost < {filters.costs};"
        return QUERY

    def __create_connection(self) -> bigquery.Client:
        return bigquery.Client()
