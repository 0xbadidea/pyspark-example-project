from pyspark.sql.types import *

schema_event_details = StructType(
    [
        StructField("_EntitySubType", StringType(), True),
        StructField("_EntityType", StringType(), True),
        StructField("_EntityVersion", LongType(), True),
        StructField("_EventData", StringType(), True),
        StructField("_EventSource", StringType(), True),
        StructField("_EventSubType", StringType(), True),
        StructField("_EventTarget", StringType(), True),
        StructField("_EventTime", TimestampType(), True),
        StructField("_EventType", StringType(), True),
        StructField("_MasterOrderNumber", StringType(), True),
        StructField("_OrderAncestry", StringType(), True),
        StructField("_OrderChannel", StringType(), True),
        StructField("_OrderEnterprise", StringType(), True),
        StructField("_OrderNumber", LongType(), True),
        StructField("_OrderProcessType", StringType(), True),
        StructField("_OrderSource", StringType(), True),
        StructField("_OrderType", StringType(), True),
        StructField("_ParentOrderNumber", StringType(), True),
        StructField("_ResentFlag", StringType(), True),
        StructField("_ResentTime", StringType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_statuschanges_orderline = ArrayType(
    StructType(
        [
            StructField("_NewStatus", DoubleType(), True),
            StructField("_NewStatusDate", TimestampType(), True),
            StructField("_PrimeLineNo", LongType(), True),
            StructField("_Quantity", DoubleType(), True),
            StructField("_SubLineNo", LongType(), True),
            StructField("_VALUE", StringType(), True),
        ]
    ),
    True,
)


schema_state_changes = StructType(
    [
        StructField(
            "StatusChanges",
            StructType(
                [StructField("OrderLine", schema_statuschanges_orderline, True)]
            ),
            True,
        )
    ]
)


schema_price_info = StructType(
    [
        StructField("_ChangeInTotalAmount", DoubleType(), True),
        StructField("_Currency", StringType(), True),
        StructField("_EnterpriseCurrency", StringType(), True),
        StructField("_ReportingConversionDate", TimestampType(), True),
        StructField("_ReportingConversionRate", DoubleType(), True),
        StructField("_TotalAmount", DoubleType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)


schema_remaining_totals = StructType(
    [
        StructField("_GrandCharges", DoubleType(), True),
        StructField("_GrandDiscount", DoubleType(), True),
        StructField("_GrandTax", DoubleType(), True),
        StructField("_GrandTotal", DoubleType(), True),
        StructField("_HdrCharges", DoubleType(), True),
        StructField("_HdrDiscount", DoubleType(), True),
        StructField("_HdrTax", DoubleType(), True),
        StructField("_HdrTotal", DoubleType(), True),
        StructField("_LineSubTotal", DoubleType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_person_info_ship_to = StructType(
    [
        StructField(
            "Extn",
            StructType(
                [
                    StructField("_IRLAddressLine1", StringType(), True),
                    StructField("_IRLAddressLine2", StringType(), True),
                    StructField("_IRLAddressLine4", StringType(), True),
                    StructField("_VALUE", StringType(), True),
                ]
            ),
            True,
        ),
        StructField("_City", StringType(), True),
        StructField("_Country", StringType(), True),
        StructField("_DayPhone", StringType(), True),
        StructField("_EMailID", StringType(), True),
        StructField("_EveningPhone", StringType(), True),
        StructField("_FirstName", StringType(), True),
        StructField("_LastName", StringType(), True),
        StructField("_Latitude", DoubleType(), True),
        StructField("_Longitude", DoubleType(), True),
        StructField("_MobilePhone", LongType(), True),
        StructField("_State", StringType(), True),
        StructField("_Title", StringType(), True),
        StructField("_ZipCode", LongType(), True),
    ]
)

schema_person_info_bill_to = StructType(
    [
        StructField(
            "Extn",
            StructType(
                [
                    StructField("_IRLAddressLine1", StringType(), True),
                    StructField("_IRLAddressLine2", StringType(), True),
                    StructField("_IRLAddressLine4", StringType(), True),
                    StructField("_VALUE", StringType(), True),
                ]
            ),
            True,
        ),
        StructField("_City", StringType(), True),
        StructField("_Country", StringType(), True),
        StructField("_DayPhone", StringType(), True),
        StructField("_EMailID", StringType(), True),
        StructField("_EveningPhone", StringType(), True),
        StructField("_FirstName", StringType(), True),
        StructField("_LastName", StringType(), True),
        StructField("_Latitude", DoubleType(), True),
        StructField("_Longitude", DoubleType(), True),
        StructField("_MobilePhone", LongType(), True),
        StructField("_State", StringType(), True),
        StructField("_Title", StringType(), True),
        StructField("_ZipCode", LongType(), True),
    ]
)

schema_payment_methods = StructType(
    [
        StructField(
            "PaymentMethod",
            StructType(
                [
                    StructField(
                        "Extn",
                        StructType(
                            [
                                StructField("_ExtnCancelledAmount", DoubleType(), True),
                                StructField("_IssuerName", StringType(), True),
                                StructField("_TenderDescription", StringType(), True),
                                StructField("_VALUE", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("_AwaitingAuthInterfaceAmount", DoubleType(), True),
                    StructField("_AwaitingChargeInterfaceAmount", DoubleType(), True),
                    StructField("_ChargeSequence", LongType(), True),
                    StructField("_CheckNo", StringType(), True),
                    StructField("_CheckReference", StringType(), True),
                    StructField("_Createts", TimestampType(), True),
                    StructField("_CreditCardExpDate", StringType(), True),
                    StructField("_CreditCardName", StringType(), True),
                    StructField("_CreditCardType", StringType(), True),
                    StructField("_CustomerPONo", StringType(), True),
                    StructField("_DisplayCreditCardNo", StringType(), True),
                    StructField("_IncompletePaymentType", StringType(), True),
                    StructField("_MaxChargeLimit", DoubleType(), True),
                    StructField("_Modifyts", TimestampType(), True),
                    StructField("_PaymentKey", DoubleType(), True),
                    StructField("_PaymentReference1", StringType(), True),
                    StructField("_PaymentReference2", LongType(), True),
                    StructField("_PaymentReference3", StringType(), True),
                    StructField("_PaymentReference6", StringType(), True),
                    StructField("_PaymentType", StringType(), True),
                    StructField("_RequestedAuthAmount", DoubleType(), True),
                    StructField("_RequestedChargeAmount", DoubleType(), True),
                    StructField("_SuspendAnyMoreCharges", StringType(), True),
                    StructField("_TotalAuthorized", DoubleType(), True),
                    StructField("_TotalCharged", DoubleType(), True),
                    StructField("_TotalRefundedAmount", DoubleType(), True),
                    StructField("_UnlimitedCharges", StringType(), True),
                ]
            ),
            True,
        )
    ]
)

schema_overall_totals = StructType(
    [
        StructField("_GrandCharges", DoubleType(), True),
        StructField("_GrandDiscount", DoubleType(), True),
        StructField("_GrandTax", DoubleType(), True),
        StructField("_GrandTotal", DoubleType(), True),
        StructField("_HdrCharges", DoubleType(), True),
        StructField("_HdrDiscount", DoubleType(), True),
        StructField("_HdrTax", DoubleType(), True),
        StructField("_HdrTotal", DoubleType(), True),
        StructField("_LineSubTotal", DoubleType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_overall_totals = StructType(
    [
        StructField("_GrandCharges", DoubleType(), True),
        StructField("_GrandDiscount", DoubleType(), True),
        StructField("_GrandTax", DoubleType(), True),
        StructField("_GrandTotal", DoubleType(), True),
        StructField("_HdrCharges", DoubleType(), True),
        StructField("_HdrDiscount", DoubleType(), True),
        StructField("_HdrTax", DoubleType(), True),
        StructField("_HdrTotal", DoubleType(), True),
        StructField("_LineSubTotal", DoubleType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_schedule = StructType(
    [
        StructField("_ExpectedDeliveryDate", TimestampType(), True),
        StructField("_ExpectedShipmentDate", TimestampType(), True),
        StructField("_OrderHeaderKey", DoubleType(), True),
        StructField("_OrderLineKey", DoubleType(), True),
        StructField("_OrderLineScheduleKey", DoubleType(), True),
        StructField("_ScheduleNo", LongType(), True),
        StructField("_TagNumber", StringType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_person_info_ship_to = StructType(
    [
        StructField(
            "Extn",
            StructType(
                [
                    StructField("_IRLAddressLine1", StringType(), True),
                    StructField("_IRLAddressLine2", StringType(), True),
                    StructField("_IRLAddressLine4", StringType(), True),
                    StructField("_VALUE", StringType(), True),
                ]
            ),
            True,
        ),
        StructField("_AddressLine1", StringType(), True),
        StructField("_AddressLine2", StringType(), True),
        StructField("_AddressLine3", StringType(), True),
        StructField("_AddressLine4", StringType(), True),
        StructField("_AddressLine5", StringType(), True),
        StructField("_AddressLine6", StringType(), True),
        StructField("_AlternateEmailID", StringType(), True),
        StructField("_Beeper", StringType(), True),
        StructField("_City", StringType(), True),
        StructField("_Company", StringType(), True),
        StructField("_Country", StringType(), True),
        StructField("_DayFaxNo", StringType(), True),
        StructField("_DayPhone", StringType(), True),
        StructField("_Department", StringType(), True),
        StructField("_EMailID", StringType(), True),
        StructField("_ErrorTxt", StringType(), True),
        StructField("_EveningFaxNo", StringType(), True),
        StructField("_EveningPhone", StringType(), True),
        StructField("_FirstName", StringType(), True),
        StructField("_HttpUrl", StringType(), True),
        StructField("_JobTitle", StringType(), True),
        StructField("_LastName", StringType(), True),
        StructField("_Latitude", DoubleType(), True),
        StructField("_Longitude", DoubleType(), True),
        StructField("_MiddleName", StringType(), True),
        StructField("_MobilePhone", LongType(), True),
        StructField("_OtherPhone", StringType(), True),
        StructField("_PersonID", StringType(), True),
        StructField("_PersonInfoKey", DoubleType(), True),
        StructField("_PreferredShipAddress", StringType(), True),
        StructField("_State", StringType(), True),
        StructField("_Suffix", StringType(), True),
        StructField("_Title", StringType(), True),
        StructField("_UseCount", LongType(), True),
        StructField("_VerificationStatus", StringType(), True),
        StructField("_ZipCode", LongType(), True),
    ]
)


schema_order_statuses = StructType(
    [
        StructField(
            "OrderStatus",
            StructType(
                [
                    StructField(
                        "Details",
                        StructType(
                            [
                                StructField(
                                    "_ExpectedDeliveryDate", TimestampType(), True
                                ),
                                StructField("_VALUE", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField(
                        "OrderStatusTranQuantity",
                        StructType(
                            [
                                StructField("_StatusQty", DoubleType(), True),
                                StructField("_TotalQuantity", DoubleType(), True),
                                StructField("_TransactionalUOM", StringType(), True),
                                StructField("_VALUE", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("_Createprogid", StringType(), True),
                    StructField("_Createts", TimestampType(), True),
                    StructField("_Createuserid", StringType(), True),
                    StructField("_ExpectedShipmentDate", TimestampType(), True),
                    StructField("_Lockid", LongType(), True),
                    StructField("_Modifyprogid", StringType(), True),
                    StructField("_Modifyts", TimestampType(), True),
                    StructField("_Modifyuserid", StringType(), True),
                    StructField("_OrderHeaderKey", DoubleType(), True),
                    StructField("_OrderLineKey", DoubleType(), True),
                    StructField("_OrderLineScheduleKey", DoubleType(), True),
                    StructField("_OrderReleaseStatusKey", DoubleType(), True),
                    StructField("_PipelineKey", DoubleType(), True),
                    StructField("_ShipNode", StringType(), True),
                    StructField("_Status", DoubleType(), True),
                    StructField("_StatusDate", TimestampType(), True),
                    StructField("_StatusDescription", StringType(), True),
                    StructField("_StatusQty", DoubleType(), True),
                    StructField("_TotalQuantity", DoubleType(), True),
                    StructField("_isHistory", StringType(), True),
                ]
            ),
            True,
        )
    ]
)

schema_order_line_tran_quantity = StructType(
    [
        StructField("_OrderedQty", DoubleType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_line_taxes = StructType(
    [
        StructField(
            "LineTax",
            ArrayType(
                StructType(
                    [
                        StructField("_ChargeCategory", StringType(), True),
                        StructField("_ChargeName", StringType(), True),
                        StructField("_ChargeNameKey", DoubleType(), True),
                        StructField("_InvoicedTax", DoubleType(), True),
                        StructField("_Reference1", StringType(), True),
                        StructField("_Reference2", StringType(), True),
                        StructField("_Reference3", DoubleType(), True),
                        StructField("_RemainingTax", DoubleType(), True),
                        StructField("_Tax", DoubleType(), True),
                        StructField("_TaxName", StringType(), True),
                        StructField("_TaxPercentage", DoubleType(), True),
                        StructField("_VALUE", StringType(), True),
                    ]
                ),
                True,
            ),
            True,
        )
    ]
)

schema_line_remaining_totals = StructType(
    [
        StructField("_AdditionalLinePriceTotal", DoubleType(), True),
        StructField("_Charges", DoubleType(), True),
        StructField("_Discount", DoubleType(), True),
        StructField("_ExtendedPrice", DoubleType(), True),
        StructField("_LineTotal", DoubleType(), True),
        StructField("_OptionPrice", DoubleType(), True),
        StructField("_PricingQty", DoubleType(), True),
        StructField("_Tax", DoubleType(), True),
        StructField("_UnitPrice", DoubleType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_line_price_info = StructType(
    [
        StructField("_DisplayUnitPrice", DoubleType(), True),
        StructField("_IsPriceLocked", StringType(), True),
        StructField("_LineTotal", DoubleType(), True),
        StructField("_ListPrice", DoubleType(), True),
        StructField("_UnitPrice", DoubleType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_line_overall_totals = StructType(
    [
        StructField("_Charges", DoubleType(), True),
        StructField("_Discount", DoubleType(), True),
        StructField("_ExtendedPrice", DoubleType(), True),
        StructField("_LineTotal", DoubleType(), True),
        StructField("_OptionPrice", DoubleType(), True),
        StructField("_PricingQty", DoubleType(), True),
        StructField("_Tax", DoubleType(), True),
        StructField("_UnitPrice", DoubleType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_line_invoiced_totals = StructType(
    [
        StructField("_AdditionalLinePriceTotal", DoubleType(), True),
        StructField("_Charges", DoubleType(), True),
        StructField("_Discount", DoubleType(), True),
        StructField("_ExtendedPrice", DoubleType(), True),
        StructField("_LineTotal", DoubleType(), True),
        StructField("_OptionPrice", DoubleType(), True),
        StructField("_PricingQty", DoubleType(), True),
        StructField("_Tax", DoubleType(), True),
        StructField("_UnitPrice", DoubleType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_chare_name_details = StructType(
    [
        StructField("_Description", StringType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_charge_category_details = StructType(
    [
        StructField("_ChargeCategoryKey", DoubleType(), True),
        StructField("_ConsiderForProfitMargin", StringType(), True),
        StructField("_Description", StringType(), True),
        StructField("_IsBillable", StringType(), True),
        StructField("_IsDiscount", StringType(), True),
        StructField("_IsRefundable", StringType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_line_charge = StructType(
    [
        StructField("ChargeCategoryDetails", schema_charge_category_details, True),
        StructField("ChargeNameDetails", schema_chare_name_details, True),
        StructField("_AmountFromAddnlLinePrices", DoubleType(), True),
        StructField("_ChargeAmount", DoubleType(), True),
        StructField("_ChargeCategory", StringType(), True),
        StructField("_ChargeName", StringType(), True),
        StructField("_ChargeNameKey", DoubleType(), True),
        StructField("_ChargePerLine", DoubleType(), True),
        StructField("_ChargePerUnit", DoubleType(), True),
        StructField("_InvoicedChargeAmount", DoubleType(), True),
        StructField("_InvoicedChargePerLine", DoubleType(), True),
        StructField("_InvoicedChargePerUnit", DoubleType(), True),
        StructField("_IsBillable", StringType(), True),
        StructField("_IsDiscount", StringType(), True),
        StructField("_IsManual", StringType(), True),
        StructField("_IsShippingCharge", StringType(), True),
        StructField("_Reference", DoubleType(), True),
        StructField("_RemainingChargeAmount", DoubleType(), True),
        StructField("_RemainingChargePerLine", DoubleType(), True),
        StructField("_RemainingChargePerUnit", DoubleType(), True),
    ]
)

schema_kit_lines = StructType(
    [
        StructField("_NumberOfKitLines", LongType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_item_details = StructType(
    [
        StructField(
            "ClassificationCodes",
            StructType(
                [
                    StructField("_CommodityCode", StringType(), True),
                    StructField("_VALUE", StringType(), True),
                ]
            ),
            True,
        ),
        StructField(
            "PrimaryInformation",
            StructType(
                [
                    StructField("_Description", StringType(), True),
                    StructField("_ItemType", StringType(), True),
                    StructField("_ShortDescription", StringType(), True),
                    StructField("_UnitHeight", DoubleType(), True),
                    StructField("_UnitLength", DoubleType(), True),
                    StructField("_UnitWeight", DoubleType(), True),
                    StructField("_UnitWidth", DoubleType(), True),
                    StructField("_VALUE", StringType(), True),
                ]
            ),
            True,
        ),
        StructField("_CanUseAsServiceTool", StringType(), True),
        StructField("_Createprogid", StringType(), True),
        StructField("_Createts", TimestampType(), True),
        StructField("_Createuserid", StringType(), True),
        StructField("_DisplayItemId", StringType(), True),
        StructField("_GlobalItemID", StringType(), True),
        StructField("_InheritAttributesFromClassification", StringType(), True),
        StructField("_IsShippingCntr", StringType(), True),
        StructField("_ItemGroupCode", StringType(), True),
        StructField("_ItemID", StringType(), True),
        StructField("_ItemKey", DoubleType(), True),
        StructField("_Lockid", LongType(), True),
        StructField("_MaxModifyTS", TimestampType(), True),
        StructField("_Modifyprogid", StringType(), True),
        StructField("_Modifyts", TimestampType(), True),
        StructField("_Modifyuserid", StringType(), True),
        StructField("_OrganizationCode", StringType(), True),
        StructField("_UnitOfMeasure", StringType(), True),
    ]
)

schema_item = StructType(
    [
        StructField("_ItemDesc", StringType(), True),
        StructField("_ItemID", StringType(), True),
        StructField("_ItemShortDesc", StringType(), True),
        StructField("_ProductClass", StringType(), True),
        StructField("_ProductLine", StringType(), True),
        StructField("_UnitCost", DoubleType(), True),
        StructField("_UnitOfMeasure", StringType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_orderlines_extn = StructType(
    [
        StructField("MarkDownDetailList", StringType(), True),
        StructField("_ArticleDesc", StringType(), True),
        StructField("_Brand", LongType(), True),
        StructField("_BuyerConfirmationName", StringType(), True),
        StructField("_ConsigneeContactNumber", LongType(), True),
        StructField("_DeliveryTimeFrom", TimestampType(), True),
        StructField("_DeliveryTimeTo", TimestampType(), True),
        StructField("_ExtnAssocLine", LongType(), True),
        StructField("_ExtnESite", StringType(), True),
        StructField("_ExtnIsEWaste", StringType(), True),
        StructField("_ExtnOrigLineTotal", DoubleType(), True),
        StructField("_ExtnReturnedQty", LongType(), True),
        StructField("_InvoiceLineDeliveryTypes", StringType(), True),
        StructField("_MaterialType", StringType(), True),
        StructField("_OriginalReqDeliveryDate", TimestampType(), True),
        StructField("_POSRefNo", StringType(), True),
        StructField("_PreOrderItem", StringType(), True),
        StructField("_PromotionAmt", LongType(), True),
        StructField("_PromotionAmt2", DoubleType(), True),
        StructField("_PromotionID", StringType(), True),
        StructField("_TMSConfirmOrder", LongType(), True),
        StructField("_TMSLMDFCID", StringType(), True),
        StructField("_TMSOrderType", StringType(), True),
        StructField("_TMSReservationID", LongType(), True),
    ]
)

schema_additional_addresses = StructType(
    [
        StructField("_NumberOfAdditionalAddresses", LongType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_instructions = StructType(
    [
        StructField("_NumberOfInstructions", LongType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_notes = StructType(
    [
        StructField("_NumberOfNotes", LongType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_order_line = StructType(
    [
        StructField("AdditionalAddresses", schema_additional_addresses, True),
        StructField("Extn", schema_orderlines_extn, True),
        StructField("Instructions", schema_instructions, True),
        StructField("Item", schema_item, True),
        StructField("ItemDetails", schema_item_details, True),
        StructField("KitLines", schema_kit_lines, True),
        StructField(
            "LineCharges",
            StructType([StructField("LineCharge", schema_line_charge, True)]),
            True,
        ),
        StructField("LineInvoicedTotals", schema_line_invoiced_totals, True),
        StructField("LineOverallTotals", schema_line_overall_totals, True),
        StructField("LinePriceInfo", schema_line_price_info, True),
        StructField("LineRemainingTotals", schema_line_remaining_totals, True),
        StructField("LineTaxes", schema_line_taxes, True),
        StructField("Notes", schema_notes, True),
        StructField("OrderLineTranQuantity", schema_order_line_tran_quantity, True),
        StructField("OrderStatuses", schema_order_statuses, True),
        StructField("PersonInfoShipTo", schema_person_info_ship_to, True),
        StructField("References", StringType(), True),
        StructField(
            "Schedules",
            StructType([StructField("Schedule", schema_schedule, True)]),
            True,
        ),
        StructField("ShipmentLines", StringType(), True),
        StructField("_AllocationDate", DateType(), True),
        StructField("_CarrierAccountNo", StringType(), True),
        StructField("_CarrierServiceCode", StringType(), True),
        StructField("_ConditionVariable1", StringType(), True),
        StructField("_Createts", TimestampType(), True),
        StructField("_CustomerLinePONo", StringType(), True),
        StructField("_CustomerPONo", StringType(), True),
        StructField("_DeliveryCode", StringType(), True),
        StructField("_DeliveryMethod", StringType(), True),
        StructField("_DepartmentCode", StringType(), True),
        StructField("_FreightTerms", StringType(), True),
        StructField("_FulfillmentType", StringType(), True),
        StructField("_HasDeliveryLines", StringType(), True),
        StructField("_HoldFlag", StringType(), True),
        StructField("_HoldReasonCode", StringType(), True),
        StructField("_ImportLicenseNo", StringType(), True),
        StructField("_InvoicedQty", DoubleType(), True),
        StructField("_IsBundleParent", StringType(), True),
        StructField("_ItemGroupCode", StringType(), True),
        StructField("_KitCode", StringType(), True),
        StructField("_LineSeqNo", DoubleType(), True),
        StructField("_LineType", StringType(), True),
        StructField("_MaxLineStatus", DoubleType(), True),
        StructField("_MaxLineStatusDesc", StringType(), True),
        StructField("_MinLineStatus", DoubleType(), True),
        StructField("_MinLineStatusDesc", StringType(), True),
        StructField("_Modifyts", TimestampType(), True),
        StructField("_OpenQty", DoubleType(), True),
        StructField("_OrderHeaderKey", DoubleType(), True),
        StructField("_OrderLineKey", DoubleType(), True),
        StructField("_OrderedQty", DoubleType(), True),
        StructField("_OriginalOrderedQty", DoubleType(), True),
        StructField("_OtherCharges", DoubleType(), True),
        StructField("_PackListType", StringType(), True),
        StructField("_PersonalizeCode", StringType(), True),
        StructField("_PersonalizeFlag", StringType(), True),
        StructField("_PickableFlag", StringType(), True),
        StructField("_PrimeLineNo", LongType(), True),
        StructField("_PromisedApptEndDate", TimestampType(), True),
        StructField("_PromisedApptStartDate", TimestampType(), True),
        StructField("_Purpose", StringType(), True),
        StructField("_RemainingQty", DoubleType(), True),
        StructField("_ReqDeliveryDate", TimestampType(), True),
        StructField("_ReservationID", StringType(), True),
        StructField("_ReservationPool", StringType(), True),
        StructField("_ReturnReason", StringType(), True),
        StructField("_SCAC", StringType(), True),
        StructField("_ScacAndService", StringType(), True),
        StructField("_ScacAndServiceKey", StringType(), True),
        StructField("_ShipNode", StringType(), True),
        StructField("_ShipTogetherNo", StringType(), True),
        StructField("_SplitQty", DoubleType(), True),
        StructField("_Status", StringType(), True),
        StructField("_StatusQuantity", DoubleType(), True),
        StructField("_SubLineNo", LongType(), True),
        StructField("_TransactionalLineId", StringType(), True),
        StructField("_isHistory", StringType(), True),
    ]
)

schema_order_lines = StructType(
    [StructField("OrderLine", ArrayType(schema_order_line), True)]
)


schema_invoiced_totals = StructType(
    [
        StructField("_GrandCharges", DoubleType(), True),
        StructField("_GrandDiscount", DoubleType(), True),
        StructField("_GrandTax", DoubleType(), True),
        StructField("_GrandTotal", DoubleType(), True),
        StructField("_HdrCharges", DoubleType(), True),
        StructField("_HdrDiscount", DoubleType(), True),
        StructField("_HdrTax", DoubleType(), True),
        StructField("_HdrTotal", DoubleType(), True),
        StructField("_LineSubTotal", DoubleType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_person_info = StructType(
    [
        StructField(
            "Extn",
            StructType(
                [
                    StructField("_IRLAddressLine1", StringType(), True),
                    StructField("_IRLAddressLine2", StringType(), True),
                    StructField("_IRLAddressLine3", StringType(), True),
                    StructField("_IRLAddressLine4", StringType(), True),
                    StructField("_VALUE", StringType(), True),
                ]
            ),
        ),
        StructField("_AlternateEmailID", StringType(), True),
        StructField("_Beeper", StringType(), True),
        StructField("_City", StringType(), True),
        StructField("_Country", StringType(), True),
        StructField("_State", StringType(), True),
    ]
)

schema_customer_additional_address = StructType(
    [
        StructField(
            "CustomerAdditionalAddress",
            StructType(
                [
                    StructField("PersonInfo", schema_person_info, True),
                    StructField("_AddressType", StringType(), True),
                    StructField("_Createprogid", StringType(), True),
                    StructField("_Createts", TimestampType(), True),
                    StructField("_Createuserid", StringType(), True),
                    StructField("_CustomerAdditionalAddressID", StringType(), True),
                    StructField("_CustomerAdditionalAddressKey", DoubleType(), True),
                    StructField("_CustomerContactKey", DoubleType(), True),
                    StructField("_CustomerKey", DoubleType(), True),
                    StructField("_IsInherited", StringType(), True),
                    StructField("_Lockid", LongType(), True),
                    StructField("_Modifyprogid", StringType(), True),
                    StructField("_Modifyts", TimestampType(), True),
                    StructField("_Modifyuserid", StringType(), True),
                    StructField("_PersonInfoKey", DoubleType(), True),
                ]
            ),
            True,
        )
    ]
)

schema_customer_contact = StructType(
    [
        StructField(
            "CustomerAdditionalAddressList", schema_customer_additional_address, True
        ),
        StructField("_Company", StringType(), True),
        StructField("_CustomerContactID", StringType(), True),
        StructField("_DayPhone", LongType(), True),
        StructField("_EmailID", StringType(), True),
        StructField("_EveningPhone", StringType(), True),
        StructField("_FirstName", StringType(), True),
        StructField("_LastName", StringType(), True),
        StructField("_MobilePhone", LongType(), True),
        StructField("_Title", StringType(), True),
    ]
)

schema_customer = StructType(
    [
        StructField(
            "CustomerContactList",
            StructType([StructField("CustomerContact", schema_customer_contact, True)]),
            True,
        ),
        StructField(
            "Extn",
            StructType(
                [
                    StructField("_ContactPersonName", StringType(), True),
                    StructField("_DoNotDisturb", StringType(), True),
                    StructField("_Gender", StringType(), True),
                    StructField("_TataFlag", StringType(), True),
                    StructField("_VALUE", StringType(), True),
                ]
            ),
            True,
        ),
        StructField("_CustomerID", StringType(), True),
        StructField("_CustomerType", LongType(), True),
        StructField("_Status", LongType(), True),
    ]
)

schema_payment_method = StructType(
    [
        StructField("_AwaitingAuthInterfaceAmount", DoubleType(), True),
        StructField("_AwaitingChargeInterfaceAmount", DoubleType(), True),
        StructField("_ChargeSequence", LongType(), True),
        StructField("_CheckNo", StringType(), True),
        StructField("_CheckReference", StringType(), True),
        StructField("_CreditCardExpDate", StringType(), True),
        StructField("_CreditCardName", StringType(), True),
        StructField("_CreditCardType", StringType(), True),
        StructField("_CustomerPONo", StringType(), True),
        StructField("_DisplayCreditCardNo", StringType(), True),
        StructField("_IncompletePaymentType", StringType(), True),
        StructField("_MaxChargeLimit", DoubleType(), True),
        StructField("_PaymentKey", DoubleType(), True),
        StructField("_PaymentReference1", StringType(), True),
        StructField("_PaymentReference2", LongType(), True),
        StructField("_PaymentReference3", StringType(), True),
        StructField("_PaymentType", StringType(), True),
        StructField("_RequestedAuthAmount", DoubleType(), True),
        StructField("_RequestedChargeAmount", DoubleType(), True),
        StructField("_SuspendAnyMoreCharges", StringType(), True),
        StructField("_TotalAuthorized", DoubleType(), True),
        StructField("_TotalCharged", DoubleType(), True),
        StructField("_TotalRefundedAmount", DoubleType(), True),
        StructField("_UnlimitedCharges", StringType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)


schema_credit_card_transactions = StructType(
    [
        StructField(
            "CreditCardTransaction",
            StructType(
                [
                    StructField("_AuthAmount", DoubleType(), True),
                    StructField("_AuthAvs", StringType(), True),
                    StructField("_AuthCode", StringType(), True),
                    StructField("_AuthReturnCode", StringType(), True),
                    StructField("_AuthReturnFlag", StringType(), True),
                    StructField("_AuthReturnMessage", StringType(), True),
                    StructField("_AuthTime", TimestampType(), True),
                    StructField("_ChargeTransactionKey", DoubleType(), True),
                    StructField("_CreditCardTransactionKey", DoubleType(), True),
                    StructField("_InternalReturnCode", StringType(), True),
                    StructField("_InternalReturnFlag", StringType(), True),
                    StructField("_InternalReturnMessage", StringType(), True),
                    StructField("_ParentKey", StringType(), True),
                    StructField("_Reference1", StringType(), True),
                    StructField("_Reference2", StringType(), True),
                    StructField("_RequestId", StringType(), True),
                    StructField("_TranAmount", DoubleType(), True),
                    StructField("_TranRequestTime", TimestampType(), True),
                    StructField("_TranReturnCode", StringType(), True),
                    StructField("_TranReturnFlag", StringType(), True),
                    StructField("_TranReturnMessage", StringType(), True),
                    StructField("_TranType", StringType(), True),
                    StructField("_VALUE", StringType(), True),
                ]
            ),
            True,
        )
    ]
)

schema_charge_transaction_detail = StructType(
    [
        StructField("CreditCardTransactions", schema_credit_card_transactions, True),
        StructField("PaymentMethod", schema_payment_method, True),
        StructField("_AuditTransactionID", StringType(), True),
        StructField("_AuthorizationExpirationDate", TimestampType(), True),
        StructField("_AuthorizationID", StringType(), True),
        StructField("_BookAmount", DoubleType(), True),
        StructField("_ChargeTransactionKey", DoubleType(), True),
        StructField("_ChargeType", StringType(), True),
        StructField("_CollectionDate", TimestampType(), True),
        StructField("_CreditAmount", DoubleType(), True),
        StructField("_DebitAmount", DoubleType(), True),
        StructField("_DistributedAmount", DoubleType(), True),
        StructField("_HoldAgainstBook", StringType(), True),
        StructField("_OpenAuthorizedAmount", DoubleType(), True),
        StructField("_OrderHeaderKey", DoubleType(), True),
        StructField("_OrderInvoiceKey", StringType(), True),
        StructField("_PaymentKey", DoubleType(), True),
        StructField("_RequestAmount", DoubleType(), True),
        StructField("_SettledAmount", DoubleType(), True),
        StructField("_Status", StringType(), True),
        StructField("_TransactionDate", TimestampType(), True),
        StructField("_UserExitStatus", StringType(), True),
    ]
)

schema_charge_transaction_details = StructType(
    [
        StructField("ChargeTransactionDetail", schema_charge_transaction_detail, True),
        StructField("_AdditionalExpectedAuthorizations", DoubleType(), True),
        StructField("_TotalCredits", DoubleType(), True),
        StructField("_TotalDebits", DoubleType(), True),
        StructField("_TotalOpenAuthorizations", DoubleType(), True),
        StructField("_TotalOpenBookings", DoubleType(), True),
        StructField("_TotalTransferredIn", DoubleType(), True),
        StructField("_TotalTransferredOut", DoubleType(), True),
    ]
)

schema_order_person_info_ship_to = StructType(
    [
        StructField("_City", StringType(), True),
        StructField("_Country", StringType(), True),
        StructField("_EMailID", StringType(), True),
        StructField("_DayPhone", StringType(), True),
        StructField("_EveningPhone", StringType(), True),
        StructField("_FirstName", StringType(), True),
        StructField("_LastName", StringType(), True),
        StructField("_Latitude", DoubleType(), True),
        StructField("_Longitude", DoubleType(), True),
        StructField("_MobilePhone", LongType(), True),
        StructField("_State", StringType(), True),
        StructField("_Title", StringType(), True),
        StructField("_ZipCode", LongType(), True),
        StructField(
            "Extn",
            StructType(
                [
                    StructField("_IRLAddressLine1", StringType(), True),
                    StructField("_IRLAddressLine2", StringType(), True),
                    StructField("_IRLAddressLine4", StringType(), True),
                    StructField("_VALUE", StringType(), True),
                ]
            ),
            True,
        ),
    ]
)


schema_order = StructType(
    [
        StructField("AdditionalAddresses", schema_additional_addresses, True),
        StructField(
            "ChargeTransactionDetails", schema_charge_transaction_details, True
        ),
        StructField("Customer", schema_customer, True),
        StructField(
            "Extn",
            StructType(
                [
                    StructField("_ExtnChannelOrderNo", LongType(), True),
                    StructField("_ExtnManualOrderReadyForConfirm", StringType(), True),
                    StructField("_SaleDate", TimestampType(), True),
                    StructField("_VALUE", StringType(), True),
                ]
            ),
            True,
        ),
        StructField("HeaderCharges", StringType(), True),
        StructField("Instructions", schema_instructions, True),
        StructField("InvoicedTotals", schema_invoiced_totals, True),
        StructField("Notes", schema_notes, True),
        StructField("OrderHoldTypes", StringType(), True),
        StructField("OrderLines", schema_order_lines, True),
        StructField("OverallTotals", schema_overall_totals, True),
        StructField("PaymentMethods", schema_payment_methods, True),
        StructField("PersonInfoBillTo", schema_person_info_bill_to, True),
        StructField("PersonInfoShipTo", schema_order_person_info_ship_to, True),
        StructField("PriceInfo", schema_price_info, True),
        StructField("RemainingTotals", schema_remaining_totals, True),
        StructField("Shipments", StringType(), True),
        StructField("_CarrierAccountNo", StringType(), True),
        StructField("_CarrierServiceCode", StringType(), True),
        StructField("_ChargeActualFreightFlag", StringType(), True),
        StructField("_Createts", TimestampType(), True),
        StructField("_CustomerContactID", StringType(), True),
        StructField("_CustomerPONo", StringType(), True),
        StructField("_DeliveryCode", StringType(), True),
        StructField("_Division", StringType(), True),
        StructField("_DocumentType", LongType(), True),
        StructField("_DraftOrderFlag", StringType(), True),
        StructField("_EnterpriseCode", StringType(), True),
        StructField("_EntryType", StringType(), True),
        StructField("_FreightTerms", StringType(), True),
        StructField("_HoldFlag", StringType(), True),
        StructField("_HoldReasonCode", StringType(), True),
        StructField("_MaxOrderStatus", DoubleType(), True),
        StructField("_MaxOrderStatusDesc", StringType(), True),
        StructField("_MinOrderStatus", LongType(), True),
        StructField("_MinOrderStatusDesc", StringType(), True),
        StructField("_Modifyts", TimestampType(), True),
        StructField("_NotifyAfterShipmentFlag", StringType(), True),
        StructField("_OrderDate", TimestampType(), True),
        StructField("_OrderHeaderKey", DoubleType(), True),
        StructField("_OrderName", StringType(), True),
        StructField("_OrderNo", LongType(), True),
        StructField("_OrderType", StringType(), True),
        StructField("_OriginalTax", DoubleType(), True),
        StructField("_OriginalTotalAmount", DoubleType(), True),
        StructField("_OtherCharges", DoubleType(), True),
        StructField("_Override", StringType(), True),
        StructField("_PaymentStatus", StringType(), True),
        StructField("_PersonalizeCode", StringType(), True),
        StructField("_PriorityCode", StringType(), True),
        StructField("_PriorityNumber", LongType(), True),
        StructField("_Purpose", StringType(), True),
        StructField("_SCAC", StringType(), True),
        StructField("_ScacAndService", StringType(), True),
        StructField("_ScacAndServiceKey", StringType(), True),
        StructField("_SearchCriteria1", StringType(), True),
        StructField("_SearchCriteria2", StringType(), True),
        StructField("_SellerOrganizationCode", StringType(), True),
        StructField("_SourcingClassification", StringType(), True),
        StructField("_Status", StringType(), True),
        StructField("_TaxExemptFlag", StringType(), True),
        StructField("_TaxExemptionCertificate", StringType(), True),
        StructField("_TaxJurisdiction", StringType(), True),
        StructField("_TaxPayerId", StringType(), True),
        StructField("_TermsCode", StringType(), True),
        StructField("_TotalAdjustmentAmount", DoubleType(), True),
        StructField("_isHistory", StringType(), True),
    ]
)

schema_current_state = StructType([StructField("Order", schema_order, True)])

payload_schema = StructType(
    [
        StructField("CurrentState", schema_current_state, True),
        StructField("EventDetails", schema_event_details, True),
        StructField("StateChanges", schema_state_changes, True),
        StructField("_corrupt_record", StringType(), True),
    ]
)
