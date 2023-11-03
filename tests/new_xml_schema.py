from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    LongType,
    DoubleType,
    TimestampType,
    ArrayType,
    DateType,
)

schema_person_info_bill_to = StructType(
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
        StructField("_Createprogid", StringType(), True),
        StructField("_Createts", StringType(), True),
        StructField("_Createuserid", StringType(), True),
        StructField("_DayFaxNo", StringType(), True),
        StructField("_DayPhone", StringType(), True),
        StructField("_Department", StringType(), True),
        StructField("_EMailID", StringType(), True),
        StructField("_ErrorTxt", StringType(), True),
        StructField("_EveningFaxNo", StringType(), True),
        StructField("_EveningPhone", StringType(), True),
        StructField("_FirstName", StringType(), True),
        StructField("_HttpUrl", StringType(), True),
        StructField("_IsAddressVerified", StringType(), True),
        StructField("_IsCommercialAddress", StringType(), True),
        StructField("_JobTitle", StringType(), True),
        StructField("_LastName", StringType(), True),
        StructField("_Latitude", DoubleType(), True),
        StructField("_Lockid", StringType(), True),
        StructField("_Longitude", DoubleType(), True),
        StructField("_MiddleName", StringType(), True),
        StructField("_MobilePhone", LongType(), True),
        StructField("_Modifyprogid", StringType(), True),
        StructField("_Modifyts", StringType(), True),
        StructField("_Modifyuserid", StringType(), True),
        StructField("_OtherPhone", StringType(), True),
        StructField("_PersonID", StringType(), True),
        StructField("_PersonInfoKey", StringType(), True),
        StructField("_PreferredShipAddress", StringType(), True),
        StructField("_State", StringType(), True),
        StructField("_Suffix", StringType(), True),
        StructField("_Title", StringType(), True),
        StructField("_UseCount", StringType(), True),
        StructField("_VerificationStatus", StringType(), True),
        StructField("_ZipCode", LongType(), True),
        StructField("_isHistory", StringType(), True),
    ]
)


schema_order_person_info_ship_to = StructType(
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
        StructField("_Createprogid", StringType(), True),
        StructField("_Createts", StringType(), True),
        StructField("_Createuserid", StringType(), True),
        StructField("_DayFaxNo", StringType(), True),
        StructField("_DayPhone", StringType(), True),
        StructField("_Department", StringType(), True),
        StructField("_EMailID", StringType(), True),
        StructField("_ErrorTxt", StringType(), True),
        StructField("_EveningFaxNo", StringType(), True),
        StructField("_EveningPhone", StringType(), True),
        StructField("_FirstName", StringType(), True),
        StructField("_HttpUrl", StringType(), True),
        StructField("_IsAddressVerified", StringType(), True),
        StructField("_IsCommercialAddress", StringType(), True),
        StructField("_JobTitle", StringType(), True),
        StructField("_LastName", StringType(), True),
        StructField("_Latitude", DoubleType(), True),
        StructField("_Lockid", StringType(), True),
        StructField("_Longitude", DoubleType(), True),
        StructField("_MiddleName", StringType(), True),
        StructField("_MobilePhone", LongType(), True),
        StructField("_Modifyprogid", StringType(), True),
        StructField("_Modifyts", StringType(), True),
        StructField("_Modifyuserid", StringType(), True),
        StructField("_OtherPhone", StringType(), True),
        StructField("_PersonID", StringType(), True),
        StructField("_PersonInfoKey", StringType(), True),
        StructField("_PreferredShipAddress", StringType(), True),
        StructField("_State", StringType(), True),
        StructField("_Suffix", StringType(), True),
        StructField("_Title", StringType(), True),
        StructField("_UseCount", StringType(), True),
        StructField("_VerificationStatus", StringType(), True),
        StructField("_ZipCode", LongType(), True),
        StructField("_isHistory", StringType(), True),
    ]
)


schema_price_info = StructType(
    [
        StructField("_ChangeInTotalAmount", StringType(), True),
        StructField("_Currency", StringType(), True),
        StructField("_EnterpriseCurrency", StringType(), True),
        StructField("_ReportingConversionDate", StringType(), True),
        StructField("_ReportingConversionRate", StringType(), True),
        StructField("_TotalAmount", StringType(), True),
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

schema_additional_addresses = StructType(
    [
        StructField("_NumberOfAdditionalAddresses", LongType(), True),
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
            True,
        ),
        StructField("_AlternateEmailID", StringType(), True),
        StructField("_Beeper", StringType(), True),
        StructField("_City", StringType(), True),
        StructField("_Country", StringType(), True),
        StructField("_State", StringType(), True),
        StructField("_ZipCode", StringType(), True),
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
                    StructField("_IsBillTo", StringType(), True),
                    StructField("_IsDefaultBillTo", StringType(), True),
                    StructField("_IsDefaultShipTo", StringType(), True),
                    StructField("_IsDefaultSoldTo", StringType(), True),
                    StructField("_IsInherited", StringType(), True),
                    StructField("_IsShipTo", StringType(), True),
                    StructField("_IsSoldTo", StringType(), True),
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
        StructField("_DateOfBirth", StringType(), True),
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
                    StructField("_Aadhar", StringType(), True),
                    StructField("_Age", StringType(), True),
                    StructField("_Anniversary", StringType(), True),
                    StructField("_ContactPersonName", StringType(), True),
                    StructField("_DoNotDisturb", StringType(), True),
                    StructField("_GST", StringType(), True),
                    StructField("_Gender", StringType(), True),
                    StructField("_MaritalStatus", StringType(), True),
                    StructField("_Occupation", StringType(), True),
                    StructField("_PAN", StringType(), True),
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


schema_header_charges = StructType(
    [
        StructField(
            "HeaderCharge",
            StructType(
                [
                    StructField("_ChargeAmount", StringType(), True),
                    StructField("_ChargeCategory", StringType(), True),
                    StructField("_ChargeName", StringType(), True),
                    StructField("_ChargeNameKey", StringType(), True),
                    StructField("_InvoicedChargeAmount", StringType(), True),
                    StructField("_IsBillable", StringType(), True),
                    StructField("_IsDiscount", StringType(), True),
                    StructField("_Reference", StringType(), True),
                    StructField("_RemainingChargeAmount", StringType(), True),
                    StructField("_VALUE", StringType(), True),
                ]
            ),
            True,
        )
    ]
)

StructType(
    [
        StructField("_NumberOfInstructions", StringType(), True),
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
        StructField(
            "Note",
            StructType(
                [
                    StructField("_NoteText", StringType(), True),
                    StructField("_VALUE", StringType(), True),
                ]
            ),
            True,
        ),
        StructField("_NumberOfNotes", StringType(), True),
    ]
)

schema_order_hold_types = StructType(
    [
        StructField(
            "OrderHoldType",
            StructType(
                [
                    StructField("_HoldType", StringType(), True),
                    StructField("_ReasonText", StringType(), True),
                    StructField("_Status", StringType(), True),
                    StructField("_TransactionId", StringType(), True),
                    StructField("_VALUE", StringType(), True),
                ]
            ),
            True,
        )
    ]
)


schema_payment_details_list = StructType(
    [
        StructField(
            "PaymentDetails",
            StructType(
                [
                    StructField("_ChargeType", StringType(), True),
                    StructField("_ProcessedAmount", StringType(), True),
                    StructField("_Reference1", StringType(), True),
                    StructField("_VALUE", StringType(), True),
                ]
            ),
            True,
        )
    ]
)

schema_payment_methods_extn = StructType(
    [
        StructField("_EMITenure", StringType(), True),
        StructField("_EMIType", StringType(), True),
        StructField("_ExtnCancelledAmount", StringType(), True),
        StructField("_ExtnEMIVendor", StringType(), True),
        StructField("_ExtnOmsExternalCreatets", StringType(), True),
        StructField("_ExtnOmsExternalModifyts", StringType(), True),
        StructField("_ExtnPOSPaymentReconNo", StringType(), True),
        StructField("_ExtnPublishToSAP", StringType(), True),
        StructField("_IssuerName", StringType(), True),
        StructField("_TenderDescription", StringType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_payment_methods = StructType(
    [
        StructField(
            "PaymentMethod",
            StructType(
                [
                    StructField("Extn", schema_payment_methods_extn, True),
                    StructField(
                        "PaymentDetailsList", schema_payment_details_list, True
                    ),
                    StructField("_AwaitingAuthInterfaceAmount", StringType(), True),
                    StructField("_AwaitingChargeInterfaceAmount", StringType(), True),
                    StructField("_ChargeSequence", StringType(), True),
                    StructField("_CheckNo", StringType(), True),
                    StructField("_CheckReference", StringType(), True),
                    StructField("_Createts", StringType(), True),
                    StructField("_CreditCardExpDate", StringType(), True),
                    StructField("_CreditCardName", StringType(), True),
                    StructField("_CreditCardType", StringType(), True),
                    StructField("_CustomerPONo", StringType(), True),
                    StructField("_DisplayCreditCardNo", StringType(), True),
                    StructField("_IncompletePaymentType", StringType(), True),
                    StructField("_MaxChargeLimit", StringType(), True),
                    StructField("_Modifyts", StringType(), True),
                    StructField("_PaymentKey", StringType(), True),
                    StructField("_PaymentReference1", StringType(), True),
                    StructField("_PaymentReference2", StringType(), True),
                    StructField("_PaymentReference3", StringType(), True),
                    StructField("_PaymentReference4", StringType(), True),
                    StructField("_PaymentReference5", StringType(), True),
                    StructField("_PaymentReference6", StringType(), True),
                    StructField("_PaymentReference7", StringType(), True),
                    StructField("_PaymentReference8", StringType(), True),
                    StructField("_PaymentReference9", StringType(), True),
                    StructField("_PaymentType", StringType(), True),
                    StructField("_RequestedAuthAmount", StringType(), True),
                    StructField("_RequestedChargeAmount", StringType(), True),
                    StructField("_SuspendAnyMoreCharges", StringType(), True),
                    StructField("_TotalAuthorized", StringType(), True),
                    StructField("_TotalCharged", StringType(), True),
                    StructField("_TotalRefundedAmount", StringType(), True),
                    StructField("_UnlimitedCharges", StringType(), True),
                ]
            ),
            True,
        )
    ]
)

schema_charge_transaction_detail = StructType(
    [
        StructField("CreditCardTransactions", schema_credit_card_transactions, True),
        StructField("PaymentMethod", schema_payment_methods, True),
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


schema_shipment_tag_serials = StructType(
    [
        StructField("ShipmentTagSerial", StringType(), True),
        StructField("_TotalNumberOfRecords", StringType(), True),
    ]
)

schema_container_details = StructType(
    [
        StructField(
            "ContainerDetail",
            StructType(
                [StructField("ShipmentTagSerials", schema_shipment_tag_serials, True)]
            ),
            True,
        ),
        StructField("_TotalNumberOfRecords", StringType(), True),
    ]
)

schema_containers = StructType(
    [
        StructField(
            "Container",
            StructType(
                [
                    StructField("ContainerDetails", schema_container_details, True),
                    StructField("_TrackingNo", StringType(), True),
                ]
            ),
            True,
        ),
        StructField("_TotalNumberOfRecords", StringType(), True),
    ]
)

schema_shipments_extn = StructType(
    [
        StructField("_DeliveredBy", StringType(), True),
        StructField("_DeliveredMode", StringType(), True),
        StructField("_ExtnChannel", StringType(), True),
        StructField("_ExtnDeliveryFailureReason", StringType(), True),
        StructField("_ExtnEnteredBy", StringType(), True),
        StructField("_ExtnInvoiceNo", StringType(), True),
        StructField("_ExtnIsLinkedRO", StringType(), True),
        StructField("_ExtnIsLinkedTradeIn", StringType(), True),
        StructField("_ExtnIsSTSFlag", StringType(), True),
        StructField("_ExtnIsValidSTS", StringType(), True),
        StructField("_ExtnSTStoreCode", StringType(), True),
        StructField("_ExtnTMSShipmentNo", StringType(), True),
        StructField("_ExtnTradeInShipmentNo", StringType(), True),
        StructField("_TPInvoiceRetryCount", StringType(), True),
        StructField("_TPInvoiceSent", StringType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_shipment_lines = StructType(
    [
        StructField(
            "ShipmentLine",
            StructType(
                [
                    StructField(
                        "ShipmentTagSerials",
                        StructType(
                            [StructField("ShipmentTagSerial", StringType(), True)]
                        ),
                        True,
                    )
                ]
            ),
            True,
        )
    ]
)

schema_shipments = StructType(
    [
        StructField(
            "Shipment",
            StructType(
                [
                    StructField("Containers", schema_containers, True),
                    StructField("Extn", schema_shipments_extn, True),
                    StructField("ShipmentLines", schema_shipment_lines, True),
                    StructField("_ActualFreightCharge", StringType(), True),
                    StructField("_ActualShipmentDate", StringType(), True),
                    StructField("_AllowOverage", StringType(), True),
                    StructField("_AssignedToUserId", StringType(), True),
                    StructField("_AssociationAction", StringType(), True),
                    StructField("_BBNMinVolume", StringType(), True),
                    StructField("_BBNMinWeight", StringType(), True),
                    StructField("_BillToAddressKey", StringType(), True),
                    StructField("_BillToCustomerId", StringType(), True),
                    StructField("_BreakBulkLoadKey", StringType(), True),
                    StructField("_CODPayMethod", StringType(), True),
                    StructField("_CarrierAccountNo", StringType(), True),
                    StructField("_CarrierServiceCode", StringType(), True),
                    StructField("_CarrierType", StringType(), True),
                    StructField("_Code", StringType(), True),
                    StructField("_CommercialValue", StringType(), True),
                    StructField("_Currency", StringType(), True),
                    StructField("_DeliveryCode", StringType(), True),
                    StructField("_DeliveryMethod", StringType(), True),
                    StructField("_DeliveryTS", StringType(), True),
                    StructField("_DestinationZone", StringType(), True),
                    StructField("_DoNotVerifyCaseContent", StringType(), True),
                    StructField("_DoNotVerifyPalletContent", StringType(), True),
                    StructField("_DocumentType", StringType(), True),
                    StructField("_DownLoadCount", StringType(), True),
                    StructField("_EnterpriseCode", StringType(), True),
                    StructField("_EspCheckRequired", StringType(), True),
                    StructField("_ExpectedDeliveryDate", StringType(), True),
                    StructField("_ExpectedShipmentDate", StringType(), True),
                    StructField("_ExportTaxpayerID", StringType(), True),
                    StructField("_FreightTerms", StringType(), True),
                    StructField("_FromAddressKey", StringType(), True),
                    StructField("_FromAppointment", StringType(), True),
                    StructField("_HasOtherShipments", StringType(), True),
                    StructField("_HazardousMaterialFlag", StringType(), True),
                    StructField("_ITDate", StringType(), True),
                    StructField("_IsPackProcessComplete", StringType(), True),
                    StructField("_IsPackingRequired", StringType(), True),
                    StructField("_IsPackingRequiredWithContents", StringType(), True),
                    StructField("_IsProductPlacingComplete", StringType(), True),
                    StructField("_IsShipmentLevelIntegration", StringType(), True),
                    StructField("_IsSingleOrder", StringType(), True),
                    StructField("_LinesEntered", StringType(), True),
                    StructField("_Lockid", StringType(), True),
                    StructField("_ManuallyEntered", StringType(), True),
                    StructField("_NextAlertTs", StringType(), True),
                    StructField("_NumOfCartons", StringType(), True),
                    StructField("_NumOfPallets", StringType(), True),
                    StructField("_OrderAvailableOnSystem", StringType(), True),
                    StructField("_OriginZone", StringType(), True),
                    StructField("_OverrideManualShipmentEntry", StringType(), True),
                    StructField("_PackAndHold", StringType(), True),
                    StructField("_PackListType", StringType(), True),
                    StructField("_PickTicketPrinted", StringType(), True),
                    StructField("_PipelineKey", StringType(), True),
                    StructField("_ReleaseNo", StringType(), True),
                    StructField("_RequestedCarrierServiceCode", StringType(), True),
                    StructField("_RequestedDeliveryDate", StringType(), True),
                    StructField("_RequestedShipmentDate", StringType(), True),
                    StructField("_SCAC", StringType(), True),
                    StructField("_ScacAndService", StringType(), True),
                    StructField("_ScacAndServiceKey", StringType(), True),
                    StructField("_ScacIntegrationRequired", StringType(), True),
                    StructField("_SellerOrganizationCode", StringType(), True),
                    StructField("_ShipDate", StringType(), True),
                    StructField("_ShipMode", StringType(), True),
                    StructField("_ShipNode", StringType(), True),
                    StructField("_ShipToCustomerId", StringType(), True),
                    StructField("_ShipVia", StringType(), True),
                    StructField("_ShipmentClosedFlag", StringType(), True),
                    StructField("_ShipmentConfirmUpdatesDone", StringType(), True),
                    StructField("_ShipmentContainerizedFlag", StringType(), True),
                    StructField("_ShipmentDeliverUpdatesDone", StringType(), True),
                    StructField("_ShipmentKey", StringType(), True),
                    StructField("_ShipmentNo", StringType(), True),
                    StructField("_ShipmentPlannedFlag", StringType(), True),
                    StructField("_ShipmentSortLocationId", StringType(), True),
                    StructField("_ShipmentType", StringType(), True),
                    StructField("_Status", StringType(), True),
                    StructField("_StatusDate", StringType(), True),
                    StructField("_ToAppointment", StringType(), True),
                    StructField("_TotalActualCharge", StringType(), True),
                    StructField("_TotalEstimatedCharge", StringType(), True),
                    StructField("_TotalNumOfPickableSKUs", StringType(), True),
                    StructField("_TotalVolume", StringType(), True),
                    StructField("_TotalVolumeUOM", StringType(), True),
                    StructField("_TotalWeight", StringType(), True),
                    StructField("_TotalWeightUOM", StringType(), True),
                    StructField("_TrackingNo", StringType(), True),
                ]
            ),
            True,
        )
    ]
)

schema_orderlines_markdown_detail_list = StructType(
    [
        StructField(
            "MarkDownDetail",
            StructType(
                [
                    StructField("_Identifier", StringType(), True),
                    StructField("_MDPrice", StringType(), True),
                    StructField("_MDPriceCurrency", StringType(), True),
                    StructField("_MDPriceSign", StringType(), True),
                    StructField("_MOPrice", StringType(), True),
                    StructField("_MOPriceCurrency", StringType(), True),
                    StructField("_MOPriceSign", StringType(), True),
                    StructField("_Quantity", StringType(), True),
                    StructField("_QuantitySign", StringType(), True),
                    StructField("_QuantityUnit", StringType(), True),
                    StructField("_ReasonCode", StringType(), True),
                    StructField("_ReasonDescription", StringType(), True),
                    StructField("_VALUE", StringType(), True),
                ]
            ),
            True,
        )
    ]
)

schema_refund_status_list = StructType(
    [
        StructField(
            "RefundStatus",
            StructType(
                [
                    StructField("_AutoRefundKey", StringType(), True),
                    StructField("_AvailableDate", StringType(), True),
                    StructField("_Createts", StringType(), True),
                    StructField("_ExternalSystem", StringType(), True),
                    StructField("_ItemID", StringType(), True),
                    StructField("_Modifyts", StringType(), True),
                    StructField("_OrderNo", StringType(), True),
                    StructField("_PrimeLineNo", StringType(), True),
                    StructField("_RefundAmount", StringType(), True),
                    StructField("_RefundFailureReason", StringType(), True),
                    StructField("_RefundReason", StringType(), True),
                    StructField("_RefundReference", StringType(), True),
                    StructField("_RefundStatus", StringType(), True),
                    StructField("_RetryCount", StringType(), True),
                    StructField("_Statusts", StringType(), True),
                    StructField("_Tender", StringType(), True),
                    StructField("_TransactionID", StringType(), True),
                    StructField("_UniqueRequestID", StringType(), True),
                    StructField("_VALUE", StringType(), True),
                ]
            ),
            True,
        )
    ]
)
schema_orderlines_extn = StructType(
    [
        StructField("MarkDownDetailList", schema_orderlines_markdown_detail_list, True),
        StructField("RefundStatusList", schema_refund_status_list, True),
        StructField("_ArticleDesc", StringType(), True),
        StructField("_Brand", StringType(), True),
        StructField("_BuyerConfirmationName", StringType(), True),
        StructField("_CSSName", StringType(), True),
        StructField("_ChannelItemCode", StringType(), True),
        StructField("_ChannelTransactionID", StringType(), True),
        StructField("_ConsigneeContactNumber", StringType(), True),
        StructField("_DeliveryTimeFrom", StringType(), True),
        StructField("_DeliveryTimeTo", StringType(), True),
        StructField("_DemoFlag", StringType(), True),
        StructField("_DemoTimeFrom", StringType(), True),
        StructField("_DemoTimeTo", StringType(), True),
        StructField("_DocType", StringType(), True),
        StructField("_EDDChangeFlag", StringType(), True),
        StructField("_ExpectedDemoDate", StringType(), True),
        StructField("_ExpectedInstallationDate", StringType(), True),
        StructField("_ExtnAssocLine", StringType(), True),
        StructField("_ExtnESite", StringType(), True),
        StructField("_ExtnIsEWaste", StringType(), True),
        StructField("_ExtnOrigLineTotal", StringType(), True),
        StructField("_ExtnParentShipmentNo", StringType(), True),
        StructField("_ExtnReturnedQty", StringType(), True),
        StructField("_ExtnTradeInShipmentNo", StringType(), True),
        StructField("_InstallationFlag", StringType(), True),
        StructField("_InstallationTimeFrom", StringType(), True),
        StructField("_InstallationTimeTo", StringType(), True),
        StructField("_InvoiceLineDeliveryTypes", StringType(), True),
        StructField("_InvoiceNo", StringType(), True),
        StructField("_LookUpStores", StringType(), True),
        StructField("_MPCarrierName", StringType(), True),
        StructField("_MaterialType", StringType(), True),
        StructField("_OriginalReqDeliveryDate", StringType(), True),
        StructField("_POSRefNo", StringType(), True),
        StructField("_ParentChannelTransactionID", StringType(), True),
        StructField("_ParentLineID", StringType(), True),
        StructField("_ParentOrderNo", StringType(), True),
        StructField("_PreOrderItem", StringType(), True),
        StructField("_PriorityFlag", StringType(), True),
        StructField("_PromotionAmt", StringType(), True),
        StructField("_PromotionAmt2", StringType(), True),
        StructField("_PromotionID", StringType(), True),
        StructField("_QuantityIndicator", StringType(), True),
        StructField("_ReasonCode", StringType(), True),
        StructField("_Route", StringType(), True),
        StructField("_SalesAmountIndicator", StringType(), True),
        StructField("_SalesPerson", StringType(), True),
        StructField("_SalesPersonName", StringType(), True),
        StructField("_TMSConfirmOrder", StringType(), True),
        StructField("_TMSLMDFCID", StringType(), True),
        StructField("_TMSLMDFCName", StringType(), True),
        StructField("_TMSOrderError", StringType(), True),
        StructField("_TMSOrderType", StringType(), True),
        StructField("_TMSReservationID", StringType(), True),
        StructField("_TMSShipmentNo", StringType(), True),
        StructField("_TradeInBrand", StringType(), True),
        StructField("_TradeInCategory", StringType(), True),
        StructField("_TradeInDeliveryType", StringType(), True),
        StructField("_TradeInExchangeBonus", StringType(), True),
        StructField("_TradeInIMEI1", StringType(), True),
        StructField("_TradeInModel", StringType(), True),
        StructField("_TradeInModelNo", StringType(), True),
        StructField("_TradeInProvider", StringType(), True),
        StructField("_TradeInQuoteID", StringType(), True),
        StructField("_TradeInServiceNo", StringType(), True),
        StructField("_TradeInWorkingCondition", StringType(), True),
        StructField("_TradeinSize", StringType(), True),
        StructField("_TradeinTonnage", StringType(), True),
        StructField("_TradeinType", StringType(), True),
        StructField("_UserGivenPrimeLineNo", StringType(), True),
    ]
)


schema_instructions = StructType(
    [
        StructField(
            "Instruction",
            StructType(
                [
                    StructField("_InstructionText", StringType(), True),
                    StructField("_InstructionType", StringType(), True),
                    StructField("_VALUE", StringType(), True),
                ]
            ),
            True,
        ),
        StructField("_NumberOfInstructions", LongType(), True),
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
        StructField("_Modifyts", StringType(), True),
        StructField("_Modifyuserid", StringType(), True),
        StructField("_OrganizationCode", StringType(), True),
        StructField("_UnitOfMeasure", StringType(), True),
    ]
)


schema_kit_lines = StructType(
    [
        StructField("_NumberOfKitLines", LongType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)


# Start with "LineCharge" / schema_line_charge


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


schema_notes = StructType(
    [
        StructField(
            "Note",
            StructType(
                [
                    StructField(
                        "User",
                        StructType(
                            [
                                StructField("_Username", StringType(), True),
                                StructField("_VALUE", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("_NoteText", StringType(), True),
                    StructField("_Priority", StringType(), True),
                    StructField("_ReasonCode", StringType(), True),
                    StructField("_VisibleToAll", StringType(), True),
                ]
            ),
            True,
        ),
        StructField("_NumberOfNotes", StringType(), True),
    ]
)


schema_order_line_tran_quantity = StructType(
    [
        StructField("_OrderedQty", DoubleType(), True),
        StructField("_VALUE", StringType(), True),
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
                    StructField("_OrderReleaseKey", StringType(), True),
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

schema_person_info_ship_to = StructType(
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
            True,
        ),
        StructField("_AddressID", StringType(), True),
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
        StructField("_IsCommercialAddress", StringType(), True),
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


schema_references = StructType(
    [
        StructField(
            "Reference",
            StructType(
                [
                    StructField("_Name", StringType(), True),
                    StructField("_VALUE", StringType(), True),
                    StructField("_Value", StringType(), True),
                ]
            ),
            True,
        )
    ]
)

schema_schedules = StructType(
    [
        StructField(
            "Schedule",
            StructType(
                [
                    StructField("_ExpectedDeliveryDate", StringType(), True),
                    StructField("_ExpectedShipmentDate", StringType(), True),
                    StructField("_OrderHeaderKey", StringType(), True),
                    StructField("_OrderLineKey", StringType(), True),
                    StructField("_OrderLineScheduleKey", StringType(), True),
                    StructField("_ScheduleNo", StringType(), True),
                    StructField("_TagNumber", StringType(), True),
                    StructField("_VALUE", StringType(), True),
                ]
            ),
            True,
        )
    ]
)

schema_container_details = StructType(
    [
        StructField("_ContainerDetailsKey", StringType(), True),
        StructField("_ItemID", StringType(), True),
        StructField("_ProductClass", StringType(), True),
        StructField("_Quantity", StringType(), True),
        StructField("_ShipmentContainerKey", StringType(), True),
        StructField("_ShipmentKey", StringType(), True),
        StructField("_UnitOfMeasure", StringType(), True),
        StructField("_VALUE", StringType(), True),
        StructField("_isHistory", StringType(), True),
    ]
)


schema_shipment_lines = StructType(
    [
        StructField(
            "ShipmentLine",
            StructType(
                [
                    StructField(
                        "ContainerDetails",
                        StructType(
                            [
                                StructField(
                                    "ContainerDetail", schema_container_details, True
                                )
                            ]
                        ),
                        True,
                    ),
                    StructField("_ActualQuantity", StringType(), True),
                    StructField("_CustomerPoLineNo", StringType(), True),
                    StructField("_CustomerPoNo", StringType(), True),
                    StructField("_DocumentType", StringType(), True),
                    StructField("_ItemDesc", StringType(), True),
                    StructField("_ItemID", StringType(), True),
                    StructField("_NetWeight", StringType(), True),
                    StructField("_NetWeightUom", StringType(), True),
                    StructField("_OrderHeaderKey", StringType(), True),
                    StructField("_OrderLineKey", StringType(), True),
                    StructField("_OrderNo", StringType(), True),
                    StructField("_OrderReleaseKey", StringType(), True),
                    StructField("_OverShipQuantity", StringType(), True),
                    StructField("_PrimeLineNo", StringType(), True),
                    StructField("_ProductClass", StringType(), True),
                    StructField("_Quantity", StringType(), True),
                    StructField("_ReleaseNo", StringType(), True),
                    StructField("_Segment", StringType(), True),
                    StructField("_SegmentType", StringType(), True),
                    StructField("_ShipmentKey", StringType(), True),
                    StructField("_ShipmentLineKey", StringType(), True),
                    StructField("_ShipmentLineNo", StringType(), True),
                    StructField("_SubLineNo", StringType(), True),
                    StructField("_UnitOfMeasure", StringType(), True),
                ]
            ),
            True,
        )
    ]
)


schema_order_line = StructType(
    [
        StructField(
            "OrderLine",
            StructType(
                [
                    StructField(
                        "AdditionalAddresses", schema_additional_addresses, True
                    ),
                    StructField(
                        "BundleParentLine",
                        StructType(
                            [
                                StructField("_OrderLineKey", StringType(), True),
                                StructField("_PrimeLineNo", StringType(), True),
                                StructField("_VALUE", StringType(), True),
                            ]
                        ),
                        True,
                    ),
                    StructField("Extn", schema_orderlines_extn, True),
                    StructField("Instructions", schema_instructions, True),
                    StructField("Item", schema_item, True),
                    StructField("ItemDetails", schema_item_details, True),
                    StructField("KitLines", schema_kit_lines, True),
                    StructField(
                        "LineCharges",
                        StructType(
                            [StructField("LineCharge", schema_line_charge, True)]
                        ),
                        True,
                    ),
                    StructField(
                        "LineInvoicedTotals", schema_line_invoiced_totals, True
                    ),
                    StructField("LineOverallTotals", schema_line_overall_totals, True),
                    StructField("LinePriceInfo", schema_line_price_info, True),
                    StructField(
                        "LineRemainingTotals", schema_line_remaining_totals, True
                    ),
                    StructField("LineTaxes", schema_line_taxes, True),
                    StructField("Notes", schema_notes, True),
                    StructField(
                        "OrderLineTranQuantity", schema_order_line_tran_quantity, True
                    ),
                    StructField("OrderStatuses", schema_order_statuses, True),
                    StructField("PersonInfoShipTo", schema_person_info_ship_to, True),
                    StructField("References", schema_references, True),
                    StructField("Schedules", schema_schedules, True),
                    StructField("ShipmentLines", schema_shipment_lines, True),
                    StructField("_AllocationDate", StringType(), True),
                    StructField("_CarrierAccountNo", StringType(), True),
                    StructField("_CarrierServiceCode", StringType(), True),
                    StructField("_ConditionVariable1", StringType(), True),
                    StructField("_Createts", StringType(), True),
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
                    StructField("_InvoicedQty", StringType(), True),
                    StructField("_IsBundleParent", StringType(), True),
                    StructField("_ItemGroupCode", StringType(), True),
                    StructField("_KitCode", StringType(), True),
                    StructField("_LineSeqNo", StringType(), True),
                    StructField("_LineType", StringType(), True),
                    StructField("_MaxLineStatus", StringType(), True),
                    StructField("_MaxLineStatusDesc", StringType(), True),
                    StructField("_MinLineStatus", StringType(), True),
                    StructField("_MinLineStatusDesc", StringType(), True),
                    StructField("_Modifyts", StringType(), True),
                    StructField("_OpenQty", StringType(), True),
                    StructField("_OrderHeaderKey", StringType(), True),
                    StructField("_OrderLineKey", StringType(), True),
                    StructField("_OrderedQty", StringType(), True),
                    StructField("_OriginalOrderedQty", StringType(), True),
                    StructField("_OtherCharges", StringType(), True),
                    StructField("_PackListType", StringType(), True),
                    StructField("_PersonalizeCode", StringType(), True),
                    StructField("_PersonalizeFlag", StringType(), True),
                    StructField("_PickableFlag", StringType(), True),
                    StructField("_PrimeLineNo", StringType(), True),
                    StructField("_ProcureFromNode", StringType(), True),
                    StructField("_PromisedApptEndDate", StringType(), True),
                    StructField("_PromisedApptStartDate", StringType(), True),
                    StructField("_Purpose", StringType(), True),
                    StructField("_RemainingQty", StringType(), True),
                    StructField("_ReqDeliveryDate", StringType(), True),
                    StructField("_ReservationID", StringType(), True),
                    StructField("_ReservationPool", StringType(), True),
                    StructField("_ReturnReason", StringType(), True),
                    StructField("_SCAC", StringType(), True),
                    StructField("_ScacAndService", StringType(), True),
                    StructField("_ScacAndServiceKey", StringType(), True),
                    StructField("_ShipNode", StringType(), True),
                    StructField("_ShipToID", StringType(), True),
                    StructField("_ShipTogetherNo", StringType(), True),
                    StructField("_SplitQty", StringType(), True),
                    StructField("_Status", StringType(), True),
                    StructField("_StatusQuantity", StringType(), True),
                    StructField("_SubLineNo", StringType(), True),
                    StructField("_TransactionalLineId", StringType(), True),
                    StructField("_isHistory", StringType(), True),
                ]
            ),
            True,
        )
    ]
)

schema_order_line = StructType(
    [
        StructField("AdditionalAddresses", schema_additional_addresses, True),
        StructField(
            "BundleParentLine",
            StructType(
                [
                    StructField("_OrderLineKey", StringType(), True),
                    StructField("_PrimeLineNo", StringType(), True),
                    StructField("_VALUE", StringType(), True),
                ]
            ),
            True,
        ),
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
        StructField("References", schema_references, True),
        StructField("Schedules", schema_schedules, True),
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
        StructField("_ProcureFromNode", StringType(), True),
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
        StructField("_ShipToID", StringType(), True),
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
                    StructField("_CashierID", StringType(), True),
                    StructField("_CashierName", StringType(), True),
                    StructField("_CommentsFromStore", StringType(), True),
                    StructField("_ExtnChannelOrderNo", StringType(), True),
                    StructField("_ExtnDty", StringType(), True),
                    StructField("_ExtnEmpID", StringType(), True),
                    StructField("_ExtnGSTNo", StringType(), True),
                    StructField("_ExtnIRNAckNo", StringType(), True),
                    StructField("_ExtnIRNNo", StringType(), True),
                    StructField("_ExtnIRNStatus", StringType(), True),
                    StructField("_ExtnInterSoreDocNo", StringType(), True),
                    StructField("_ExtnManualOrderReadyForConfirm", StringType(), True),
                    StructField("_ExtnSalesOrderNo", StringType(), True),
                    StructField("_GiftWrappingFlag", StringType(), True),
                    StructField("_MaxRepaymentDate", StringType(), True),
                    StructField("_SaleDate", StringType(), True),
                    StructField("_TillNo", StringType(), True),
                    StructField("_VALUE", StringType(), True),
                    StructField("_ZECPReason", StringType(), True),
                ]
            ),
            True,
        ),
        StructField("HeaderCharges", schema_header_charges, True),
        StructField("Instructions", schema_instructions, True),
        StructField("InvoicedTotals", schema_invoiced_totals, True),
        StructField("Notes", schema_notes, True),
        StructField("OrderHoldTypes", schema_order_hold_types, True),
        StructField(
            "OrderLines",
            StructType([StructField("OrderLine", schema_order_line, True)]),
            True,
        ),
        StructField("OverallTotals", schema_overall_totals, True),
        StructField("PaymentMethods", schema_payment_methods, True),
        StructField("PersonInfoBillTo", schema_person_info_bill_to, True),
        StructField("PersonInfoShipTo", schema_order_person_info_ship_to, True),
        StructField("PriceInfo", schema_price_info, True),
        StructField("RemainingTotals", schema_remaining_totals, True),
        StructField("Shipments", schema_shipments, True),
        StructField("_AuthorizationExpirationDate", StringType(), True),
        StructField("_BillToID", StringType(), True),
        StructField("_CarrierAccountNo", StringType(), True),
        StructField("_CarrierServiceCode", StringType(), True),
        StructField("_ChargeActualFreightFlag", StringType(), True),
        StructField("_Createts", StringType(), True),
        StructField("_CustomerContactID", StringType(), True),
        StructField("_CustomerEMailID", StringType(), True),
        StructField("_CustomerPONo", StringType(), True),
        StructField("_DeliveryCode", StringType(), True),
        StructField("_Division", StringType(), True),
        StructField("_DocumentType", StringType(), True),
        StructField("_DraftOrderFlag", StringType(), True),
        StructField("_EnteredBy", StringType(), True),
        StructField("_EnterpriseCode", StringType(), True),
        StructField("_EntryType", StringType(), True),
        StructField("_FreightTerms", StringType(), True),
        StructField("_HoldFlag", StringType(), True),
        StructField("_HoldReasonCode", StringType(), True),
        StructField("_MaxOrderStatus", StringType(), True),
        StructField("_MaxOrderStatusDesc", StringType(), True),
        StructField("_MinOrderStatus", StringType(), True),
        StructField("_MinOrderStatusDesc", StringType(), True),
        StructField("_Modifyts", StringType(), True),
        StructField("_NotifyAfterShipmentFlag", StringType(), True),
        StructField("_OrderDate", StringType(), True),
        StructField("_OrderHeaderKey", StringType(), True),
        StructField("_OrderName", StringType(), True),
        StructField("_OrderNo", StringType(), True),
        StructField("_OrderPurpose", StringType(), True),
        StructField("_OrderType", StringType(), True),
        StructField("_OriginalOrderDate", StringType(), True),
        StructField("_OriginalTax", StringType(), True),
        StructField("_OriginalTotalAmount", StringType(), True),
        StructField("_OtherCharges", StringType(), True),
        StructField("_Override", StringType(), True),
        StructField("_PaymentStatus", StringType(), True),
        StructField("_PersonalizeCode", StringType(), True),
        StructField("_PriorityCode", StringType(), True),
        StructField("_PriorityNumber", StringType(), True),
        StructField("_Purpose", StringType(), True),
        StructField("_ReqDeliveryDate", StringType(), True),
        StructField("_ReturnOrderHeaderKeyForExchange", StringType(), True),
        StructField("_SCAC", StringType(), True),
        StructField("_ScacAndService", StringType(), True),
        StructField("_ScacAndServiceKey", StringType(), True),
        StructField("_SearchCriteria1", StringType(), True),
        StructField("_SearchCriteria2", StringType(), True),
        StructField("_SellerOrganizationCode", StringType(), True),
        StructField("_ShipToID", StringType(), True),
        StructField("_SourcingClassification", StringType(), True),
        StructField("_Status", StringType(), True),
        StructField("_TaxExemptFlag", StringType(), True),
        StructField("_TaxExemptionCertificate", StringType(), True),
        StructField("_TaxJurisdiction", StringType(), True),
        StructField("_TaxPayerId", StringType(), True),
        StructField("_TermsCode", StringType(), True),
        StructField("_TotalAdjustmentAmount", StringType(), True),
        StructField("_isHistory", StringType(), True),
    ]
)


schema_current_state = StructType([StructField("Order", schema_order, True)])

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


payload_schema = StructType(
    [
        StructField("CurrentState", schema_current_state, True),
        StructField("EventDetails", schema_event_details, True),
        StructField("StateChanges", schema_state_changes, True),
        StructField("_corrupt_record", StringType(), True),
    ]
)
