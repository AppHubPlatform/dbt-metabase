from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, Mapping, Optional

from dbtmetabase._format import NullValue
from dbtmetabase.core import DbtMetabase
from dbtmetabase.manifest import Column, Group, Model

FIXTURES_PATH = Path("tests") / "fixtures"
TMP_PATH = Path("tests") / "tmp"


class MockCore(DbtMetabase):
    def __init__(self):
        super().__init__(
            manifest_path=Path("tests") / "fixtures" / "manifest.json",
            metabase_url="http://localhost:3000",
            metabase_session_id="dummy",
        )

    def read_models(self) -> Iterable[Model]:
        return MANIFEST_MODELS

    def metabase_api(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        critical: bool = True,
        **kwargs,
    ) -> Mapping:
        path_toks = f"{path.lstrip('/')}.json".split("/")
        if path_toks[0] == "api" and method == "get":
            json_path = Path.joinpath(FIXTURES_PATH, *path_toks)
            if json_path.exists():
                with open(json_path, encoding="utf-8") as f:
                    return json.load(f)
        return {}


MANIFEST_MODELS = [
    Model(
        database="TEST",
        schema="PUBLIC",
        group=Group.nodes,
        name="orders",
        description="This table has basic information about orders, as well as some derived facts based on payments",
        unique_id="model.jaffle_shop.orders",
        source=None,
        tags=[],
        columns=[
            Column(
                name="ORDER_ID",
                description="This is a unique identifier for an order",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            Column(
                name="CUSTOMER_ID",
                description="Foreign key to the customers table",
                meta_fields={},
                semantic_type="type/FK",
                visibility_type=None,
                fk_target_table="PUBLIC.CUSTOMERS",
                fk_target_field="CUSTOMER_ID",
            ),
            Column(
                name="ORDER_DATE",
                description="Date (UTC) that the order was placed",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            Column(
                name="STATUS",
                description="Orders can be one of the following statuses:\n\n| status         | description                                                                                                            |\n|----------------|------------------------------------------------------------------------------------------------------------------------|\n| placed         | The order has been placed but has not yet left the warehouse                                                           |\n| shipped        | The order has ben shipped to the customer and is currently in transit                                                  |\n| completed      | The order has been received by the customer                                                                            |\n| return_pending | The customer has indicated that they would like to return the order, but it has not yet been received at the warehouse |\n| returned       | The order has been returned by the customer and received at the warehouse                                              |",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            Column(
                name="AMOUNT",
                description="Total amount (AUD) of the order",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            Column(
                name="CREDIT_CARD_AMOUNT",
                description="Amount of the order (AUD) paid for by credit card",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            Column(
                name="COUPON_AMOUNT",
                description="Amount of the order (AUD) paid for by coupon",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            Column(
                name="BANK_TRANSFER_AMOUNT",
                description="Amount of the order (AUD) paid for by bank transfer",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            Column(
                name="GIFT_CARD_AMOUNT",
                description="Amount of the order (AUD) paid for by gift card",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
        ],
    ),
    Model(
        database="TEST",
        schema="PUBLIC",
        group=Group.nodes,
        name="customers",
        description="This table has basic information about a customer, as well as some derived facts based on a customer's orders",
        unique_id="model.jaffle_shop.customers",
        source=None,
        tags=[],
        columns=[
            Column(
                name="CUSTOMER_ID",
                description="This is a unique identifier for a customer",
                meta_fields={},
                semantic_type=None,  # This is a PK field, should not be detected as FK
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            Column(
                name="FIRST_NAME",
                description="Customer's first name. PII.",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            Column(
                name="LAST_NAME",
                description="Customer's last name. PII.",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            Column(
                name="FIRST_ORDER",
                description="Date (UTC) of a customer's first order",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            Column(
                name="MOST_RECENT_ORDER",
                description="Date (UTC) of a customer's most recent order",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            Column(
                name="NUMBER_OF_ORDERS",
                description="Count of the number of orders a customer has placed",
                meta_fields={},
                semantic_type=NullValue,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            Column(
                name="CUSTOMER_LIFETIME_VALUE",
                description="Total value (AUD) of a customer's orders",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
        ],
    ),
    Model(
        database="TEST",
        schema="PUBLIC",
        group=Group.nodes,
        name="stg_orders",
        description="",
        unique_id="model.jaffle_shop.stg_orders",
        source=None,
        tags=[],
        columns=[
            Column(
                name="ORDER_ID",
                description="",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            Column(
                name="STATUS",
                description="",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
        ],
    ),
    Model(
        database="TEST",
        schema="PUBLIC",
        group=Group.nodes,
        name="stg_payments",
        description="",
        unique_id="model.jaffle_shop.stg_payments",
        source=None,
        tags=[],
        columns=[
            Column(
                name="PAYMENT_ID",
                description="",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            Column(
                name="PAYMENT_METHOD",
                description="",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
        ],
    ),
    Model(
        database="TEST",
        schema="PUBLIC",
        group=Group.nodes,
        name="stg_customers",
        description="",
        unique_id="model.jaffle_shop.stg_customers",
        source=None,
        tags=[],
        columns=[
            Column(
                name="CUSTOMER_ID",
                description="",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            )
        ],
    ),
]


# MODELS = [
#     Model(
#         database="TEST",
#         schema="PUBLIC",
#         group=Group.nodes,
#         name="orders",
#         description="This table has basic information about orders, as well as some derived facts based on payments",
#         unique_id="model.jaffle_shop.orders",
#         tags=[],
#         columns=[
#             Column(
#                 name="ORDER_ID",
#                 description="This is a unique identifier for an order",
#                 meta_fields={},
#                 semantic_type=None,
#                 visibility_type=None,
#                 fk_target_table=None,
#                 fk_target_field=None,
#             ),
#             Column(
#                 name="CUSTOMER_ID",
#                 description="Foreign key to the customers table",
#                 meta_fields={},
#                 semantic_type="type/FK",
#                 visibility_type=None,
#                 fk_target_table="PUBLIC.CUSTOMERS",
#                 fk_target_field="CUSTOMER_ID",
#             ),
#             Column(
#                 name="ORDER_DATE",
#                 description="Date (UTC) that the order was placed",
#                 meta_fields={},
#                 semantic_type=None,
#                 visibility_type=None,
#                 fk_target_table=None,
#                 fk_target_field=None,
#             ),
#             Column(
#                 name="STATUS",
#                 description="Orders can be one of the following statuses:\n\n| status         | description                                                                                                            |\n|----------------|------------------------------------------------------------------------------------------------------------------------|\n| placed         | The order has been placed but has not yet left the warehouse                                                           |\n| shipped        | The order has ben shipped to the customer and is currently in transit                                                  |\n| completed      | The order has been received by the customer                                                                            |\n| return_pending | The customer has indicated that they would like to return the order, but it has not yet been received at the warehouse |\n| returned       | The order has been returned by the customer and received at the warehouse                                              |",
#                 meta_fields={},
#                 semantic_type=None,
#                 visibility_type=None,
#                 fk_target_table=None,
#                 fk_target_field=None,
#             ),
#             Column(
#                 name="AMOUNT",
#                 description="Total amount (AUD) of the order",
#                 meta_fields={},
#                 semantic_type=None,
#                 visibility_type=None,
#                 fk_target_table=None,
#                 fk_target_field=None,
#             ),
#             Column(
#                 name="CREDIT_CARD_AMOUNT",
#                 description="Amount of the order (AUD) paid for by credit card",
#                 meta_fields={},
#                 semantic_type=None,
#                 visibility_type=None,
#                 fk_target_table=None,
#                 fk_target_field=None,
#             ),
#             Column(
#                 name="COUPON_AMOUNT",
#                 description="Amount of the order (AUD) paid for by coupon",
#                 meta_fields={},
#                 semantic_type=None,
#                 visibility_type=None,
#                 fk_target_table=None,
#                 fk_target_field=None,
#             ),
#             Column(
#                 name="BANK_TRANSFER_AMOUNT",
#                 description="Amount of the order (AUD) paid for by bank transfer",
#                 meta_fields={},
#                 semantic_type=None,
#                 visibility_type=None,
#                 fk_target_table=None,
#                 fk_target_field=None,
#             ),
#             Column(
#                 name="GIFT_CARD_AMOUNT",
#                 description="Amount of the order (AUD) paid for by gift card",
#                 meta_fields={},
#                 semantic_type=None,
#                 visibility_type=None,
#                 fk_target_table=None,
#                 fk_target_field=None,
#             ),
#         ],
#     ),
#     Model(
#         database="TEST",
#         schema="PUBLIC",
#         group=Group.nodes,
#         name="customers",
#         description="This table has basic information about a customer, as well as some derived facts based on a customer's orders",
#         unique_id="model.jaffle_shop.customers",
#         tags=[],
#         columns=[
#             Column(
#                 name="CUSTOMER_ID",
#                 description="This is a unique identifier for a customer",
#                 meta_fields={},
#                 semantic_type="type/FK",
#                 visibility_type=None,
#                 fk_target_table="PUBLIC.orders",
#                 fk_target_field="CUSTOMER_ID",
#             ),
#             Column(
#                 name="FIRST_NAME",
#                 description="Customer's first name. PII.",
#                 meta_fields={},
#                 semantic_type=None,
#                 visibility_type=None,
#                 fk_target_table=None,
#                 fk_target_field=None,
#             ),
#             Column(
#                 name="LAST_NAME",
#                 description="Customer's last name. PII.",
#                 meta_fields={},
#                 semantic_type=None,
#                 visibility_type=None,
#                 fk_target_table=None,
#                 fk_target_field=None,
#             ),
#             Column(
#                 name="FIRST_ORDER",
#                 description="Date (UTC) of a customer's first order",
#                 meta_fields={},
#                 semantic_type=None,
#                 visibility_type=None,
#                 fk_target_table=None,
#                 fk_target_field=None,
#             ),
#             Column(
#                 name="MOST_RECENT_ORDER",
#                 description="Date (UTC) of a customer's most recent order",
#                 meta_fields={},
#                 semantic_type=None,
#                 visibility_type=None,
#                 fk_target_table=None,
#                 fk_target_field=None,
#             ),
#             Column(
#                 name="NUMBER_OF_ORDERS",
#                 description="Count of the number of orders a customer has placed",
#                 meta_fields={"display_name": "order_count"},
#                 semantic_type=None,
#                 visibility_type=None,
#                 fk_target_table=None,
#                 fk_target_field=None,
#             ),
#             Column(
#                 name="CUSTOMER_LIFETIME_VALUE",
#                 description="Total value (AUD) of a customer's orders",
#                 meta_fields={},
#                 semantic_type=None,
#                 visibility_type=None,
#                 fk_target_table=None,
#                 fk_target_field=None,
#             ),
#         ],
#     ),
#     Model(
#         database="TEST",
#         schema="PUBLIC",
#         group=Group.nodes,
#         name="stg_orders",
#         description="",
#         tags=[],
#         columns=[
#             Column(
#                 name="ORDER_ID",
#                 description="",
#                 meta_fields={},
#                 semantic_type=None,
#                 visibility_type=None,
#                 fk_target_table=None,
#                 fk_target_field=None,
#             ),
#             Column(
#                 name="STATUS",
#                 description="",
#                 meta_fields={},
#                 semantic_type=None,
#                 visibility_type=None,
#                 fk_target_table=None,
#                 fk_target_field=None,
#             ),
#         ],
#     ),
#     Model(
#         database="TEST",
#         schema="PUBLIC",
#         group=Group.nodes,
#         name="stg_payments",
#         description="",
#         tags=[],
#         columns=[
#             Column(
#                 name="PAYMENT_ID",
#                 description="",
#                 meta_fields={},
#                 semantic_type=None,
#                 visibility_type=None,
#                 fk_target_table=None,
#                 fk_target_field=None,
#             ),
#             Column(
#                 name="PAYMENT_METHOD",
#                 description="",
#                 meta_fields={},
#                 semantic_type=None,
#                 visibility_type=None,
#                 fk_target_table=None,
#                 fk_target_field=None,
#             ),
#         ],
#     ),
#     Model(
#         database="TEST",
#         schema="PUBLIC",
#         group=Group.nodes,
#         name="stg_customers",
#         description="",
#         tags=[],
#         columns=[
#             Column(
#                 name="CUSTOMER_ID",
#                 description="",
#                 meta_fields={},
#                 semantic_type=None,
#                 visibility_type=None,
#                 fk_target_table=None,
#                 fk_target_field=None,
#             )
#         ],
#     ),
# ]