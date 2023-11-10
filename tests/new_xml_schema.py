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

schema_order_person_info_bill_To_extn = StructType(
    [
        StructField("_IRLAddressLine1", StringType(), True),
        StructField("_IRLAddressLine2", StringType(), True),
        StructField("_IRLAddressLine3", StringType(), True),
        StructField("_IRLAddressLine4", StringType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_order_person_info_bill_to = StructType(
    [
        StructField("Extn", schema_order_person_info_bill_To_extn, True),
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

schema_order_person_info_ship_to_extn = StructType(
    [
        StructField("_IRLAddressLine1", StringType(), True),
        StructField("_IRLAddressLine2", StringType(), True),
        StructField("_IRLAddressLine3", StringType(), True),
        StructField("_IRLAddressLine4", StringType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_order_person_info_ship_to = StructType(
    [
        StructField("Extn", schema_order_person_info_ship_to_extn, True),
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


schema_order_price_info = StructType(
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

schema_order_remaining_totals = StructType(
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


schema_order_overall_totals = StructType(
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


schema_order_invoiced_totals = StructType(
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

schema_person_info_extn = StructType(
    [
        StructField("_IRLAddressLine1", StringType(), True),
        StructField("_IRLAddressLine2", StringType(), True),
        StructField("_IRLAddressLine3", StringType(), True),
        StructField("_IRLAddressLine4", StringType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)


schema_person_info = StructType(
    [
        StructField("Extn", schema_person_info_extn, True),
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
)

schema_customer_additional_address = ArrayType(
    StructType(
        [
            StructField(
                "CustomerAdditionalAddress", schema_customer_additional_address, True
            )
        ]
    )
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

schema_order_customer_extn = StructType(
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
)

schema_customer_contact_list = ArrayType(
    StructType([StructField("CustomerContact", schema_customer_contact, True)])
)

schema_order_customer = StructType(
    [
        StructField("CustomerContactList", schema_customer_contact_list, True),
        StructField("Extn", schema_order_customer_extn, True),
        StructField("_CustomerID", StringType(), True),
        StructField("_CustomerType", LongType(), True),
        StructField("_Status", LongType(), True),
    ]
)

schema_order_header_charge = StructType(
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
)

schema_order_header_charges = ArrayType(
    StructType([StructField("HeaderCharge", schema_order_header_charge, True)])
)


schema_order_instructions = StructType(
    [
        StructField("_NumberOfInstructions", LongType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_order_notes = StructType(
    [
        StructField(
            "Note",
            ArrayType(
                StructType(
                    [
                        StructField("_NoteText", StringType(), True),
                        StructField("_VALUE", StringType(), True),
                    ]
                )
            ),
        ),
        StructField("_NumberOfNotes", StringType(), True),
    ]
)

schema_order_hold_type = ArrayType(
    StructType(
        [
            StructField("_HoldType", StringType(), True),
            StructField("_ReasonText", StringType(), True),
            StructField("_Status", StringType(), True),
            StructField("_TransactionId", StringType(), True),
            StructField("_VALUE", StringType(), True),
        ]
    )
)

schema_order_hold_types = StructType(
    [StructField("OrderHoldType", schema_order_hold_type, True)]
)


schema_payment_details = ArrayType(
    StructType(
        [
            StructField("_ChargeType", StringType(), True),
            StructField("_ProcessedAmount", StringType(), True),
            StructField("_Reference1", StringType(), True),
            StructField("_VALUE", StringType(), True),
        ]
    )
)

schema_payment_details_list = StructType(
    [StructField("PaymentDetails", schema_payment_details, True)]
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

schema_order_payment_method = StructType(
    [
        StructField("Extn", schema_payment_methods_extn, True),
        StructField("PaymentDetailsList", schema_payment_details_list, True),
        StructField("_Action", StringType(), True),
        StructField("_AwaitingAuthInterfaceAmount", StringType(), True),
        StructField("_AwaitingChargeInterfaceAmount", StringType(), True),
        StructField("_BillToKey", StringType(), True),
        StructField("_ChargeSequence", StringType(), True),
        StructField("_CheckNo", StringType(), True),
        StructField("_CheckReference", StringType(), True),
        StructField("_Createprogid", StringType(), True),
        StructField("_Createts", StringType(), True),
        StructField("_Createuserid", StringType(), True),
        StructField("_CreditCardExpDate", StringType(), True),
        StructField("_CreditCardName", StringType(), True),
        StructField("_CreditCardType", StringType(), True),
        StructField("_CustomerPONo", StringType(), True),
        StructField("_DisplayCreditCardNo", StringType(), True),
        StructField("_DisplayCustomerAccountNo", StringType(), True),
        StructField("_DisplayPaymentReference1", StringType(), True),
        StructField("_DisplayPrimaryAccountNo", StringType(), True),
        StructField("_DisplaySvcNo", StringType(), True),
        StructField("_ExtendedFlag", StringType(), True),
        StructField("_IncompletePaymentType", StringType(), True),
        StructField("_Lockid", StringType(), True),
        StructField("_MaxChargeLimit", StringType(), True),
        StructField("_Modifyprogid", StringType(), True),
        StructField("_Modifyts", StringType(), True),
        StructField("_Modifyuserid", StringType(), True),
        StructField("_OrderHeaderKey", StringType(), True),
        StructField("_PayMethodOverride", StringType(), True),
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
        StructField("_PaymentTypeGroup", StringType(), True),
        StructField("_PlannedRefundAmount", StringType(), True),
        StructField("_PrimaryAccountNo", StringType(), True),
        StructField("_RequestedAuthAmount", StringType(), True),
        StructField("_RequestedChargeAmount", StringType(), True),
        StructField("_RequestedRefundAmount", StringType(), True),
        StructField("_SecondaryAmount", StringType(), True),
        StructField("_SuspendAnyMoreCharges", StringType(), True),
        StructField("_TotalAltRefundedAmount", StringType(), True),
        StructField("_TotalAuthorized", StringType(), True),
        StructField("_TotalCharged", StringType(), True),
        StructField("_TotalRefundedAmount", StringType(), True),
        StructField("_UnlimitedCharges", StringType(), True),
        StructField("_isHistory", StringType(), True),
    ]
)

schema_order_payment_methods = ArrayType(
    StructType([StructField("PaymentMethod", schema_order_payment_method, True)])
)

schema_order_additional_addresses = StructType(
    [
        StructField("_NumberOfAdditionalAddresses", LongType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_credit_card_transaction = StructType(
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
)

schema_credit_card_transactions = ArrayType(
    StructType(
        [StructField("CreditCardTransaction", schema_credit_card_transaction, True)]
    )
)

schema_charge_transaction_payment_method = StructType(
    [
        StructField("_AwaitingAuthInterfaceAmount", StringType(), True),
        StructField("_AwaitingChargeInterfaceAmount", StringType(), True),
        StructField("_ChargeSequence", StringType(), True),
        StructField("_CheckNo", StringType(), True),
        StructField("_CheckReference", StringType(), True),
        StructField("_CreditCardExpDate", StringType(), True),
        StructField("_CreditCardName", StringType(), True),
        StructField("_CreditCardType", StringType(), True),
        StructField("_CustomerPONo", StringType(), True),
        StructField("_DisplayCreditCardNo", StringType(), True),
        StructField("_IncompletePaymentType", StringType(), True),
        StructField("_MaxChargeLimit", StringType(), True),
        StructField("_PaymentKey", StringType(), True),
        StructField("_PaymentReference1", StringType(), True),
        StructField("_PaymentReference2", StringType(), True),
        StructField("_PaymentReference3", StringType(), True),
        StructField("_PaymentType", StringType(), True),
        StructField("_RequestedAuthAmount", StringType(), True),
        StructField("_RequestedChargeAmount", StringType(), True),
        StructField("_SuspendAnyMoreCharges", StringType(), True),
        StructField("_TotalAuthorized", StringType(), True),
        StructField("_TotalCharged", StringType(), True),
        StructField("_TotalRefundedAmount", StringType(), True),
        StructField("_UnlimitedCharges", StringType(), True),
    ]
)

schema_charge_transaction_detail = StructType(
    [
        StructField("CreditCardTransactions", schema_credit_card_transactions, True),
        StructField("PaymentMethod", schema_charge_transaction_payment_method, True),
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

schema_order_charge_transaction_details = StructType(
    [
        StructField(
            "ChargeTransactionDetail", ArrayType(schema_charge_transaction_detail), True
        ),
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

schema_container = StructType(
    [
        StructField(
            "Container",
            ArrayType(
                StructType(
                    [
                        StructField("ContainerDetails", schema_container_details, True),
                        StructField("_TrackingNo", StringType(), True),
                    ]
                )
            ),
        )
    ]
)

schema_order_shipment_extn = StructType(
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

schema_order_shipment_container = StructType(
    [
        StructField("ContainerDetails", StringType(), True),
        StructField("_TrackingNo", StringType(), True),
    ]
)

schema_order_shipment_containers = StructType(
    [
        StructField("Container", ArrayType(schema_order_shipment_container), True),
        StructField("_TotalNumberOfRecords", StringType(), True),
    ]
)

schema_order_shipment_line_shipment_tag_serials = ArrayType(
    StructType([StructField("ShipmentTagSerial", StringType(), True)])
)

schema_order_shipment_line = StructType(
    [
        StructField(
            "ShipmentTagSerials", schema_order_shipment_line_shipment_tag_serials, True
        )
    ]
)

schema_order_shipment_lines = ArrayType(
    StructType([StructField("ShipmentLine", schema_order_shipment_line, True)])
)

schema_order_shipment = StructType(
    [
        StructField("Containers", schema_order_shipment_containers, True),
        StructField("Extn", schema_order_shipment_extn, True),
        StructField("ShipmentLines", schema_order_shipment_lines, True),
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
)

schema_order_shipments = ArrayType(
    StructType([StructField("Shipment", schema_order_shipment, True)])
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


schema_instruction = StructType(
    [
        StructField("_InstructionText", StringType(), True),
        StructField("_InstructionType", StringType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_instructions = StructType(
    [
        StructField("Instruction", ArrayType(schema_instruction), True),
        StructField("_NumberOfInstructions", LongType(), True),
    ]
)


schema_item = StructType(
    [
        StructField("_BundleFulfillmentMode", StringType(), True),
        StructField("_CostCurrency", StringType(), True),
        StructField("_CountryOfOrigin", StringType(), True),
        StructField("_CustomerItem", StringType(), True),
        StructField("_CustomerItemDesc", StringType(), True),
        StructField("_ECCNNo", StringType(), True),
        StructField("_HarmonizedCode", StringType(), True),
        StructField("_ISBN", StringType(), True),
        StructField("_ItemDesc", StringType(), True),
        StructField("_ItemID", StringType(), True),
        StructField("_ItemShortDesc", StringType(), True),
        StructField("_ItemWeight", StringType(), True),
        StructField("_ItemWeightUOM", StringType(), True),
        StructField("_ManufacturerItem", StringType(), True),
        StructField("_ManufacturerItemDesc", StringType(), True),
        StructField("_ManufacturerName", StringType(), True),
        StructField("_NMFCClass", StringType(), True),
        StructField("_NMFCCode", StringType(), True),
        StructField("_NMFCDescription", StringType(), True),
        StructField("_ProductClass", StringType(), True),
        StructField("_ProductLine", StringType(), True),
        StructField("_ScheduleBCode", StringType(), True),
        StructField("_SupplierItem", StringType(), True),
        StructField("_SupplierItemDesc", StringType(), True),
        StructField("_TaxProductCode", StringType(), True),
        StructField("_UPCCode", StringType(), True),
        StructField("_UnitCost", DoubleType(), True),
        StructField("_UnitOfMeasure", StringType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_item_details_primary_information = StructType(
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
)

schema_item_details_classification_codes = StructType(
    [
        StructField("_CommodityCode", StringType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_item_details = StructType(
    [
        StructField(
            "PrimaryInformation", schema_item_details_primary_information, True
        ),
        StructField(
            "ClassificationCodes", schema_item_details_classification_codes, True
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


schema_charge_name_details = StructType(
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
        StructField("ChargeNameDetails", schema_charge_name_details, True),
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
        StructField("_ActualPricingQty", StringType(), True),
        StructField("_DiscountPercentage", StringType(), True),
        StructField("_DiscountReference", StringType(), True),
        StructField("_DiscountType", StringType(), True),
        StructField("_DisplayUnitPrice", DoubleType(), True),
        StructField("_InvoicedLineTotal", StringType(), True),
        StructField("_InvoicedPricingQty", StringType(), True),
        StructField("_IsEligibleForShippingDiscount", StringType(), True),
        StructField("_IsLinePriceForInformationOnly", StringType(), True),
        StructField("_IsPriceLocked", StringType(), True),
        StructField("_LineTotal", DoubleType(), True),
        StructField("_ListPrice", DoubleType(), True),
        StructField("_OrderedPricingQty", StringType(), True),
        StructField("_PricingQtyConversionFactor", StringType(), True),
        StructField("_PricingQuantityStrategy", StringType(), True),
        StructField("_PricingUOM", StringType(), True),
        StructField("_RepricingQty", StringType(), True),
        StructField("_RetailPrice", StringType(), True),
        StructField("_SettledAmount", StringType(), True),
        StructField("_SettledQuantity", StringType(), True),
        StructField("_Tax", StringType(), True),
        StructField("_TaxableFlag", StringType(), True),
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

schema_line_tax = StructType(
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
)

schema_line_taxes = ArrayType(
    StructType([StructField("LineTax", schema_line_tax, True)])
)

schema_note_user = StructType(
    [
        StructField("_Username", StringType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_note = StructType(
    [
        StructField("User", schema_note_user, True),
        StructField("_NoteText", StringType(), True),
        StructField("_Priority", StringType(), True),
        StructField("_ReasonCode", StringType(), True),
        StructField("_VisibleToAll", StringType(), True),
    ]
)

schema_notes = StructType(
    [
        StructField("Note", ArrayType(schema_note), True),
        StructField("_NumberOfNotes", StringType(), True),
    ]
)
schema_order_line_tran_quantity = StructType(
    [
        StructField("_OrderedQty", DoubleType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_order_status_detail = StructType(
    [
        StructField("_ExpectedDeliveryDate", TimestampType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_order_status_tran_quantity = StructType(
    [
        StructField("_StatusQty", DoubleType(), True),
        StructField("_TotalQuantity", DoubleType(), True),
        StructField("_TransactionalUOM", StringType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_order_status = StructType(
    [
        StructField("Details", schema_order_status_detail, True),
        StructField("OrderStatusTranQuantity", schema_order_status_tran_quantity, True),
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
)

schema_order_statuses = ArrayType(
    StructType([StructField("schema_order_status", schema_order_status, True)])
)
schema_person_info_ship_to_extn = StructType(
    [
        StructField("_IRLAddressLine1", StringType(), True),
        StructField("_IRLAddressLine2", StringType(), True),
        StructField("_IRLAddressLine3", StringType(), True),
        StructField("_IRLAddressLine4", StringType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_person_info_ship_to = StructType(
    [
        StructField("Extn", schema_person_info_ship_to_extn, True),
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
        StructField("_PersonInfoKey", DoubleType(), True),
        StructField("_PreferredShipAddress", StringType(), True),
        StructField("_State", StringType(), True),
        StructField("_Suffix", StringType(), True),
        StructField("_Title", StringType(), True),
        StructField("_UseCount", LongType(), True),
        StructField("_VerificationStatus", StringType(), True),
        StructField("_ZipCode", LongType(), True),
        StructField("_isHistory", StringType(), True),
    ]
)


schema_reference = StructType(
    [
        StructField("_Name", StringType(), True),
        StructField("_VALUE", StringType(), True),
        StructField("_Value", StringType(), True),
    ]
)

schema_references = ArrayType(
    StructType([StructField("Reference", schema_reference, True)])
)
schema_schedule = StructType(
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
)

schema_schedules = ArrayType(
    StructType([StructField("Schedule", schema_schedule, True)])
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
        StructField("_isHistory", StringType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_shipment_lines_container_details = ArrayType(
    StructType([StructField("ContainerDetail", schema_container_details, True)])
)

schema_shipment_line = StructType(
    [
        StructField("ContainerDetails", schema_shipment_lines_container_details, True),
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
)

schema_shipment_lines = ArrayType(
    StructType([StructField("ShipmentLine", schema_shipment_line, True)])
)

schema_derived_from_order_lines_extn = StructType(
    [
        StructField("_ArticleDesc", StringType(), True),
        StructField("_Brand", StringType(), True),
        StructField("_BuyerConfirmationName", StringType(), True),
        StructField("_CSSName", StringType(), True),
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
        StructField("_ParentLineID", StringType(), True),
        StructField("_ParentOrderNo", StringType(), True),
        StructField("_PreOrderItem", StringType(), True),
        StructField("_PriorityFlag", StringType(), True),
        StructField("_PromotionAmt", StringType(), True),
        StructField("_PromotionAmt2", StringType(), True),
        StructField("_PromotionID", StringType(), True),
        StructField("_QuantityIndicator", StringType(), True),
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
        StructField("_TradeInIMEI1", StringType(), True),
        StructField("_TradeInModelNo", StringType(), True),
        StructField("_UserGivenPrimeLineNo", StringType(), True),
    ]
)
schema_derived_from_order_lines_item_details = StructType(
    [
        StructField(
            "PrimaryInformation",
            StructType([StructField("_ItemType", StringType(), True)]),
            True,
        ),
        StructField("ItemID", StringType(), True),
        StructField("UnitOfMeasure", StringType(), True),
    ]
)

schema_derived_from_order_lines_item = StructType(
    [
        StructField("_ItemID", StringType(), True),
        StructField("_UnitOfMeasure", StringType(), True),
    ]
)

schema_derived_from_order_lines = StructType(
    [
        StructField("Extn", schema_derived_from_order_lines_extn, True),
        StructField("ItemDetails", schema_derived_from_order_lines_item_details, True),
        StructField("Item", schema_derived_from_order_lines_item, True),
        StructField("_AddToOrderReleaseKey", StringType(), True),
        StructField("_ApptStatus", StringType(), True),
        StructField("_BackorderNotificationQty", StringType(), True),
        StructField("_BasicCapacityRequired", StringType(), True),
        StructField("_BundleParentOrderLineKey", StringType(), True),
        StructField("_CanAddServiceLines", StringType(), True),
        StructField("_CannotCompleteAfterDate", StringType(), True),
        StructField("_CannotCompleteBeforeDate", StringType(), True),
        StructField("_CannotMeetAppt", StringType(), True),
        StructField("_CapacityUOM", StringType(), True),
        StructField("_CarrierAccountNo", StringType(), True),
        StructField("_CarrierServiceCode", StringType(), True),
        StructField("_ConditionVariable1", StringType(), True),
        StructField("_ConditionVariable2", StringType(), True),
        StructField("_Createprogid", StringType(), True),
        StructField("_Createts", StringType(), True),
        StructField("_Createuserid", StringType(), True),
        StructField("_CustomerLinePONo", StringType(), True),
        StructField("_CustomerPONo", StringType(), True),
        StructField("_DeliveryCode", StringType(), True),
        StructField("_DeliveryMethod", StringType(), True),
        StructField("_DepartmentCode", StringType(), True),
        StructField("_DependencyRatio", StringType(), True),
        StructField("_EarliestDeliveryDate", StringType(), True),
        StructField("_EarliestShipDate", StringType(), True),
        StructField("_FillQuantity", StringType(), True),
        StructField("_FixedCapacityQtyPerLine", StringType(), True),
        StructField("_FixedPricingQtyPerLine", StringType(), True),
        StructField("_FreightTerms", StringType(), True),
        StructField("_FulfillmentType", StringType(), True),
        StructField("_GiftFlag", StringType(), True),
        StructField("_HoldFlag", StringType(), True),
        StructField("_HoldReasonCode", StringType(), True),
        StructField("_ImportLicenseNo", StringType(), True),
        StructField("_IntentionalBackorder", StringType(), True),
        StructField("_InvoiceBasedOnActuals", StringType(), True),
        StructField("_InvoiceComplete", StringType(), True),
        StructField("_InvoicedExtendedPrice", StringType(), True),
        StructField("_InvoicedQuantity", StringType(), True),
        StructField("_IsCapacityOverridden", StringType(), True),
        StructField("_IsCostOverridden", StringType(), True),
        StructField("_IsFirmPredefinedNode", StringType(), True),
        StructField("_IsPriceMatched", StringType(), True),
        StructField("_IsStandaloneService", StringType(), True),
        StructField("_ItemGroupCode", StringType(), True),
        StructField("_KitCode", StringType(), True),
        StructField("_KitQty", StringType(), True),
        StructField("_LineSeqNo", StringType(), True),
        StructField("_LineType", StringType(), True),
        StructField("_Lockid", StringType(), True),
        StructField("_MaintainRatio", StringType(), True),
        StructField("_Modifyprogid", StringType(), True),
        StructField("_Modifyts", StringType(), True),
        StructField("_Modifyuserid", StringType(), True),
        StructField("_OptionCapacityRequired", StringType(), True),
        StructField("_OrderClass", StringType(), True),
        StructField("_OrderHeaderKey", StringType(), True),
        StructField("_OrderLineKey", StringType(), True),
        StructField("_OrderedQty", StringType(), True),
        StructField("_OrderingUOM", StringType(), True),
        StructField("_OriginalOrderedQty", StringType(), True),
        StructField("_OtherCharges", StringType(), True),
        StructField("_OverReceiptQuantity", StringType(), True),
        StructField("_PackListType", StringType(), True),
        StructField("_ParentOfDependentGroup", StringType(), True),
        StructField("_PersonalizeCode", StringType(), True),
        StructField("_PersonalizeFlag", StringType(), True),
        StructField("_PickableFlag", StringType(), True),
        StructField("_PipelineKey", StringType(), True),
        StructField("_PricingDate", StringType(), True),
        StructField("_PrimeLineNo", StringType(), True),
        StructField("_PropagationQty", StringType(), True),
        StructField("_PropagationToParentRequired", StringType(), True),
        StructField("_Purpose", StringType(), True),
        StructField("_QuantityToSplit", StringType(), True),
        StructField("_ReceivedAsComponents", StringType(), True),
        StructField("_ReceivedQty", StringType(), True),
        StructField("_ReqDeliveryDate", StringType(), True),
        StructField("_ReservationID", StringType(), True),
        StructField("_ReservationMandatory", StringType(), True),
        StructField("_ReservationPool", StringType(), True),
        StructField("_ReturnReason", StringType(), True),
        StructField("_SCAC", StringType(), True),
        StructField("_SchedFailureReasonCode", StringType(), True),
        StructField("_Segment", StringType(), True),
        StructField("_SegmentType", StringType(), True),
        StructField("_SerialNo", StringType(), True),
        StructField("_ShipNode", StringType(), True),
        StructField("_ShipToKey", StringType(), True),
        StructField("_ShipTogetherNo", StringType(), True),
        StructField("_ShippedQuantity", StringType(), True),
        StructField("_SplitFromLineKey", StringType(), True),
        StructField("_SplitFromPrimeLineNo", StringType(), True),
        StructField("_SplitFromSubLineNo", StringType(), True),
        StructField("_SplitQty", StringType(), True),
        StructField("_Status", StringType(), True),
        StructField("_SubLineNo", StringType(), True),
        StructField("_Timezone", StringType(), True),
        StructField("_TotalQtyToCancel", StringType(), True),
        StructField("_TranDiscrepancyQty", StringType(), True),
        StructField("_TransactionalLineId", StringType(), True),
        StructField("_WaitForSeqLine", StringType(), True),
        StructField("_isHistory", StringType(), True),
    ]
)

schema_derived_from_order_extn = StructType(
    [
        StructField("_CashierID", StringType(), True),
        StructField("_CashierName", StringType(), True),
        StructField("_CommentsFromStore", StringType(), True),
        StructField("_ExtnChannelOrderNo", StringType(), True),
        StructField("_ExtnEmpID", StringType(), True),
        StructField("_ExtnEnableOrderPurge", StringType(), True),
        StructField("_ExtnGSTNo", StringType(), True),
        StructField("_ExtnIRNAckNo", StringType(), True),
        StructField("_ExtnIRNNo", StringType(), True),
        StructField("_ExtnIRNStatus", StringType(), True),
        StructField("_ExtnInterSoreDocNo", StringType(), True),
        StructField("_ExtnManualOrderReadyForConfirm", StringType(), True),
        StructField("_GiftWrappingFlag", StringType(), True),
        StructField("_MaxRepaymentDate", StringType(), True),
        StructField("_RejectedReason", StringType(), True),
        StructField("_SaleDate", StringType(), True),
        StructField("_TillNo", StringType(), True),
        StructField("_ZECPReason", StringType(), True),
    ]
)

schema_derived_from_order = StructType(
    [
        StructField("Extn", schema_derived_from_order_extn, True),
        StructField("_ActualPricingDate", StringType(), True),
        StructField("_AdjustmentInvoicePending", StringType(), True),
        StructField("_AllAddressesVerified", StringType(), True),
        StructField("_ApprovalCycle", StringType(), True),
        StructField("_AuthorizationExpirationDate", StringType(), True),
        StructField("_BillToID", StringType(), True),
        StructField("_BillToKey", StringType(), True),
        StructField("_CarrierAccountNo", StringType(), True),
        StructField("_CarrierServiceCode", StringType(), True),
        StructField("_ChainType", StringType(), True),
        StructField("_ChargeActualFreightFlag", StringType(), True),
        StructField("_ComplimentaryGiftBoxQty", StringType(), True),
        StructField("_CreatedAtNode", StringType(), True),
        StructField("_Createprogid", StringType(), True),
        StructField("_Createts", StringType(), True),
        StructField("_Createuserid", StringType(), True),
        StructField("_CustCustPONo", StringType(), True),
        StructField("_CustomerAge", StringType(), True),
        StructField("_CustomerContactID", StringType(), True),
        StructField("_CustomerEMailID", StringType(), True),
        StructField("_CustomerFirstName", StringType(), True),
        StructField("_CustomerLastName", StringType(), True),
        StructField("_CustomerPONo", StringType(), True),
        StructField("_CustomerPhoneNo", StringType(), True),
        StructField("_CustomerZipCode", StringType(), True),
        StructField("_DeliveryCode", StringType(), True),
        StructField("_Division", StringType(), True),
        StructField("_DoNotConsolidate", StringType(), True),
        StructField("_DocumentType", StringType(), True),
        StructField("_DraftOrderFlag", StringType(), True),
        StructField("_EnteredBy", StringType(), True),
        StructField("_EnterpriseCode", StringType(), True),
        StructField("_EntryType", StringType(), True),
        StructField("_ExchangeType", StringType(), True),
        StructField("_FreightTerms", StringType(), True),
        StructField("_HasDerivedChild", StringType(), True),
        StructField("_HasDerivedParent", StringType(), True),
        StructField("_HoldFlag", StringType(), True),
        StructField("_HoldReasonCode", StringType(), True),
        StructField("_InternalApp", StringType(), True),
        StructField("_InvoiceComplete", StringType(), True),
        StructField("_Lockid", StringType(), True),
        StructField("_Modifyprogid", StringType(), True),
        StructField("_Modifyts", StringType(), True),
        StructField("_Modifyuserid", StringType(), True),
        StructField("_NextAlertTs", StringType(), True),
        StructField("_NoOfAuthStrikes", StringType(), True),
        StructField("_NotifyAfterShipmentFlag", StringType(), True),
        StructField("_OrderComplete", StringType(), True),
        StructField("_OrderDate", StringType(), True),
        StructField("_OrderHeaderKey", StringType(), True),
        StructField("_OrderName", StringType(), True),
        StructField("_OrderNo", StringType(), True),
        StructField("_OrderPurpose", StringType(), True),
        StructField("_OrderType", StringType(), True),
        StructField("_OriginalTax", StringType(), True),
        StructField("_OriginalTotalAmount", StringType(), True),
        StructField("_OtherCharges", StringType(), True),
        StructField("_Override", StringType(), True),
        StructField("_PaymentStatus", StringType(), True),
        StructField("_PendingTransferIn", StringType(), True),
        StructField("_PersonalizeCode", StringType(), True),
        StructField("_PriceOrder", StringType(), True),
        StructField("_PriceProgramName", StringType(), True),
        StructField("_PriorityCode", StringType(), True),
        StructField("_PriorityNumber", StringType(), True),
        StructField("_PropagateCancellations", StringType(), True),
        StructField("_Purpose", StringType(), True),
        StructField("_ReqDeliveryDate", StringType(), True),
        StructField("_ReserveInventoryFlag", StringType(), True),
        StructField("_ReturnByGiftRecipient", StringType(), True),
        StructField("_ReturnOrderHeaderKeyForExchange", StringType(), True),
        StructField("_SCAC", StringType(), True),
        StructField("_SaleVoided", StringType(), True),
        StructField("_SearchCriteria1", StringType(), True),
        StructField("_SearchCriteria2", StringType(), True),
        StructField("_SellerOrganizationCode", StringType(), True),
        StructField("_ShipToID", StringType(), True),
        StructField("_ShipToKey", StringType(), True),
        StructField("_SourceIPAddress", StringType(), True),
        StructField("_SourcingClassification", StringType(), True),
        StructField("_TaxExemptFlag", StringType(), True),
        StructField("_TaxExemptionCertificate", StringType(), True),
        StructField("_TaxJurisdiction", StringType(), True),
        StructField("_TaxPayerId", StringType(), True),
        StructField("_TermsCode", StringType(), True),
        StructField("_TotalAdjustmentAmount", StringType(), True),
        StructField("_isHistory", StringType(), True),
    ]
)

schema_markdown_detail = StructType(
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
    ]
)

schema_order_line_extn_markdownlist = ArrayType(
    StructType([StructField("MarkDownDetail", schema_markdown_detail, True)])
)

schema_order_line_extn = StructType(
    [
        StructField("MarkDownDetailList", schema_order_line_extn_markdownlist, True),
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
        StructField("_PickUpDate", StringType(), True),
        StructField("_PreOrderItem", StringType(), True),
        StructField("_PriorityFlag", StringType(), True),
        StructField("_PromotionAmt", StringType(), True),
        StructField("_PromotionAmt2", StringType(), True),
        StructField("_PromotionID", StringType(), True),
        StructField("_QuantityIndicator", StringType(), True),
        StructField("_ReasonCode", StringType(), True),
        StructField("_ReturnDescription", StringType(), True),
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
schema_line_charges = ArrayType(
    StructType([StructField("LineCharge", schema_line_charge, True)])
)

schema_bundle_parent = StructType(
    [
        StructField("_OrderLineKey", StringType(), True),
        StructField("_PrimeLineNo", StringType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_order_line = StructType(
    [
        StructField("Instructions", schema_instructions, True),
        StructField("Item", schema_item, True),
        StructField("LineInvoicedTotals", schema_line_invoiced_totals, True),
        StructField("OrderStatuses", schema_order_statuses, True),
        StructField("ItemDetails", schema_item_details, True),
        StructField("PersonInfoShipTo", schema_person_info_ship_to, True),
        StructField("LineRemainingTotals", schema_line_remaining_totals, True),
        StructField("Schedules", schema_schedules, True),
        StructField("LineCharges", schema_line_charges, True),
        StructField("LineOverallTotals", schema_line_overall_totals, True),
        StructField("ShipmentLines", schema_shipment_lines, True),
        StructField("Extn", schema_order_line_extn, True),
        StructField("LinePriceInfo", schema_line_price_info, True),
        StructField("BundleParentLine", schema_bundle_parent, True),
        StructField("LineTaxes", schema_line_taxes, True),
        StructField("KitLines", schema_kit_lines, True),
        StructField("References", schema_references, True),
        StructField("OrderLineTranQuantity", schema_order_line_tran_quantity, True),
        StructField("Notes", schema_notes, True),
        StructField("AdditionalAddresses", schema_order_additional_addresses, True),
        StructField("DerivedFromOrderLine", schema_derived_from_order_lines, True),
        StructField("DerivedFromOrder", schema_derived_from_order, True),
        StructField("_AddToOrderReleaseKey", StringType(), True),
        StructField("_AllocationDate", DateType(), True),
        StructField("_ApptStatus", StringType(), True),
        StructField("_BackorderNotificationQty", StringType(), True),
        StructField("_BasicCapacityRequired", StringType(), True),
        StructField("_BundleParentOrderLineKey", StringType(), True),
        StructField("_CanAddServiceLines", StringType(), True),
        StructField("_CannotCompleteAfterDate", StringType(), True),
        StructField("_CannotCompleteBeforeDate", StringType(), True),
        StructField("_CannotMeetAppt", StringType(), True),
        StructField("_CapacityUOM", StringType(), True),
        StructField("_CarrierAccountNo", StringType(), True),
        StructField("_CarrierServiceCode", StringType(), True),
        StructField("_ConditionVariable1", StringType(), True),
        StructField("_ConditionVariable2", StringType(), True),
        StructField("_Createprogid", StringType(), True),
        StructField("_Createts", TimestampType(), True),
        StructField("_Createuserid", TimestampType(), True),
        StructField("_CustomerLinePONo", StringType(), True),
        StructField("_CustomerPONo", StringType(), True),
        StructField("_DeliveryCode", StringType(), True),
        StructField("_DeliveryMethod", StringType(), True),
        StructField("_DepartmentCode", StringType(), True),
        StructField("_DependencyRatio", StringType(), True),
        StructField("_DerivedFromExternalOrder", StringType(), True),
        StructField("_DerivedFromOrderHeaderKey", StringType(), True),
        StructField("_DerivedFromOrderLineKey", StringType(), True),
        StructField("_DerivedFromOrderReleaseKey", StringType(), True),
        StructField("_EarliestDeliveryDate", StringType(), True),
        StructField("_EarliestShipDate", StringType(), True),
        StructField("_FillQuantity", StringType(), True),
        StructField("_FixedCapacityQtyPerLine", StringType(), True),
        StructField("_FixedPricingQtyPerLine", StringType(), True),
        StructField("_FreightTerms", StringType(), True),
        StructField("_FulfillmentType", StringType(), True),
        StructField("_GiftFlag", StringType(), True),
        StructField("_HasDeliveryLines", StringType(), True),
        StructField("_HoldFlag", StringType(), True),
        StructField("_HoldReasonCode", StringType(), True),
        StructField("_ImportLicenseNo", StringType(), True),
        StructField("_IntentionalBackorder", StringType(), True),
        StructField("_InvoiceBasedOnActuals", StringType(), True),
        StructField("_InvoiceComplete", StringType(), True),
        StructField("_InvoicedExtendedPrice", StringType(), True),
        StructField("_InvoicedQty", DoubleType(), True),
        StructField("_InvoicedQuantity", DoubleType(), True),
        StructField("_IsBlindLine", StringType(), True),
        StructField("_IsBundleParent", StringType(), True),
        StructField("_IsCapacityOverridden", StringType(), True),
        StructField("_IsCostOverridden", StringType(), True),
        StructField("_IsFirmPredefinedNode", StringType(), True),
        StructField("_IsPriceMatched", StringType(), True),
        StructField("_IsStandaloneService", StringType(), True),
        StructField("_ItemGroupCode", StringType(), True),
        StructField("_KitCode", StringType(), True),
        StructField("_KitQty", StringType(), True),
        StructField("_LineSeqNo", DoubleType(), True),
        StructField("_LineType", StringType(), True),
        StructField("_Lockid", StringType(), True),
        StructField("_MaintainRatio", StringType(), True),
        StructField("_MaxLineStatus", StringType(), True),
        StructField("_MaxLineStatusDesc", StringType(), True),
        StructField("_MaxLineStatus", DoubleType(), True),
        StructField("_MaxLineStatusDesc", StringType(), True),
        StructField("_MinLineStatus", DoubleType(), True),
        StructField("_MinLineStatusDesc", StringType(), True),
        StructField("_Modifyprogid", StringType(), True),
        StructField("_Modifyts", TimestampType(), True),
        StructField("_Modifyuserid", StringType(), True),
        StructField("_OpenQty", DoubleType(), True),
        StructField("_OptionCapacityRequired", StringType(), True),
        StructField("_OrderClass", StringType(), True),
        StructField("_OrderHeaderKey", DoubleType(), True),
        StructField("_OrderLineKey", DoubleType(), True),
        StructField("_OrderedQty", DoubleType(), True),
        StructField("_OrderingUOM", StringType(), True),
        StructField("_OriginalOrderedQty", DoubleType(), True),
        StructField("_OtherCharges", DoubleType(), True),
        StructField("_OverReceiptQuantity", StringType(), True),
        StructField("_PackListType", StringType(), True),
        StructField("_ParentOfDependentGroup", StringType(), True),
        StructField("_PersonalizeCode", StringType(), True),
        StructField("_PersonalizeFlag", StringType(), True),
        StructField("_PickableFlag", StringType(), True),
        StructField("_PipelineKey", StringType(), True),
        StructField("_PricingDate", StringType(), True),
        StructField("_PrimeLineNo", StringType(), True),
        StructField("_ProcureFromNode", StringType(), True),
        StructField("_PromisedApptEndDate", StringType(), True),
        StructField("_PromisedApptStartDate", StringType(), True),
        StructField("_PropagationQty", StringType(), True),
        StructField("_PropagationToParentRequired", StringType(), True),
        StructField("_Purpose", StringType(), True),
        StructField("_QuantityToSplit", StringType(), True),
        StructField("_ReceivedAsComponents", StringType(), True),
        StructField("_ReceivedQty", StringType(), True),
        StructField("_RemainingQty", StringType(), True),
        StructField("_ReqDeliveryDate", StringType(), True),
        StructField("_ReservationID", StringType(), True),
        StructField("_ReservationMandatory", StringType(), True),
        StructField("_ReservationPool", StringType(), True),
        StructField("_ReturnReason", StringType(), True),
        StructField("_SCAC", StringType(), True),
        StructField("_ScacAndService", StringType(), True),
        StructField("_ScacAndServiceKey", StringType(), True),
        StructField("_SchedFailureReasonCode", StringType(), True),
        StructField("_Segment", StringType(), True),
        StructField("_SegmentType", StringType(), True),
        StructField("_SerialNo", StringType(), True),
        StructField("_ShipNode", StringType(), True),
        StructField("_ShipToID", StringType(), True),
        StructField("_ShipToKey", StringType(), True),
        StructField("_ShipTogetherNo", StringType(), True),
        StructField("_ShippedQuantity", StringType(), True),
        StructField("_SplitFromLineKey", StringType(), True),
        StructField("_SplitFromPrimeLineNo", StringType(), True),
        StructField("_SplitFromSubLineNo", StringType(), True),
        StructField("_SplitQty", StringType(), True),
        StructField("_Status", StringType(), True),
        StructField("_StatusQuantity", StringType(), True),
        StructField("_SubLineNo", StringType(), True),
        StructField("_Timezone", StringType(), True),
        StructField("_TotalQtyToCancel", StringType(), True),
        StructField("_TranDiscrepancyQty", StringType(), True),
        StructField("_TransactionalLineId", StringType(), True),
        StructField("_WaitForSeqLine", StringType(), True),
        StructField("_isHistory", StringType(), True),
    ]
)

schema_order_lines = ArrayType(
    StructType([StructField("OrderLine", schema_order_line, True)])
)

schema_return_order_for_exchange_extn = StructType(
    [
        StructField("_CommentsFromStore", StringType(), True),
        StructField("ExtnChannelOrderNo", StringType(), True),
        StructField("ExtnEmpID", StringType(), True),
        StructField("ExtnEnableOrderPurge", StringType(), True),
        StructField("ExtnGSTNo", StringType(), True),
        StructField("ExtnIRNStatus", StringType(), True),
        StructField("ExtnInterSoreDocNo", StringType(), True),
        StructField("ExtnManualOrderReadyForConfirm", StringType(), True),
        StructField("ExtnRetnInvoiceOrderNo", StringType(), True),
        StructField("ExtnSalesInvoiceOrderDate", StringType(), True),
        StructField("ExtnSalesInvoiceOrderNo", StringType(), True),
        StructField("SaleDate", StringType(), True),
        StructField("ZECPReason", StringType(), True),
    ]
)

schema_return_order_for_exchange = StructType(
    [
        StructField("Extn", schema_return_order_for_exchange_extn),
        StructField("_ActualPricingDate", StringType(), True),
        StructField("_AdjustmentInvoicePending", StringType(), True),
        StructField("_AllAddressesVerified", StringType(), True),
        StructField("_ApprovalCycle", StringType(), True),
        StructField("_AuthorizationExpirationDate", StringType(), True),
        StructField("_BillToKey", StringType(), True),
        StructField("_CarrierAccountNo", StringType(), True),
        StructField("_CarrierServiceCode", StringType(), True),
        StructField("_ChainType", StringType(), True),
        StructField("_ChargeActualFreightFlag", StringType(), True),
        StructField("_ComplimentaryGiftBoxQty", StringType(), True),
        StructField("_CreatedAtNode", StringType(), True),
        StructField("_Createprogid", StringType(), True),
        StructField("_Createts", StringType(), True),
        StructField("_Createuserid", StringType(), True),
        StructField("_CustCustPONo", StringType(), True),
        StructField("_CustomerAge", StringType(), True),
        StructField("_CustomerContactID", StringType(), True),
        StructField("_CustomerEMailID", StringType(), True),
        StructField("_CustomerFirstName", StringType(), True),
        StructField("_CustomerLastName", StringType(), True),
        StructField("_CustomerPONo", StringType(), True),
        StructField("_CustomerPhoneNo", StringType(), True),
        StructField("_CustomerZipCode", StringType(), True),
        StructField("_DeliveryCode", StringType(), True),
        StructField("_Division", StringType(), True),
        StructField("_DoNotConsolidate", StringType(), True),
        StructField("_DocumentType", StringType(), True),
        StructField("_DraftOrderFlag", StringType(), True),
        StructField("_EnteredBy", StringType(), True),
        StructField("_EnterpriseCode", StringType(), True),
        StructField("_EntryType", StringType(), True),
        StructField("_FreightTerms", StringType(), True),
        StructField("_HasDerivedChild", StringType(), True),
        StructField("_HasDerivedParent", StringType(), True),
        StructField("_HoldFlag", StringType(), True),
        StructField("_HoldReasonCode", StringType(), True),
        StructField("_InternalApp", StringType(), True),
        StructField("_InvoiceComplete", StringType(), True),
        StructField("_Lockid", StringType(), True),
        StructField("_MaxOrderStatus", StringType(), True),
        StructField("_MinOrderStatus", StringType(), True),
        StructField("_Modifyprogid", StringType(), True),
        StructField("_Modifyts", StringType(), True),
        StructField("_Modifyuserid", StringType(), True),
        StructField("_NextAlertTs", StringType(), True),
        StructField("_NoOfAuthStrikes", StringType(), True),
        StructField("_NotifyAfterShipmentFlag", StringType(), True),
        StructField("_OrderComplete", StringType(), True),
        StructField("_OrderDate", StringType(), True),
        StructField("_OrderHeaderKey", StringType(), True),
        StructField("_OrderName", StringType(), True),
        StructField("_OrderNo", StringType(), True),
        StructField("_OrderType", StringType(), True),
        StructField("_OriginalTax", StringType(), True),
        StructField("_OriginalTotalAmount", StringType(), True),
        StructField("_OtherCharges", StringType(), True),
        StructField("_Override", StringType(), True),
        StructField("_PaymentStatus", StringType(), True),
        StructField("_PendingTransferIn", StringType(), True),
        StructField("_PersonalizeCode", StringType(), True),
        StructField("_PriceOrder", StringType(), True),
        StructField("_PriceProgramName", StringType(), True),
        StructField("_PriorityCode", StringType(), True),
        StructField("_PriorityNumber", StringType(), True),
        StructField("_PropagateCancellations", StringType(), True),
        StructField("_Purpose", StringType(), True),
        StructField("_ReserveInventoryFlag", StringType(), True),
        StructField("_ReturnByGiftRecipient", StringType(), True),
        StructField("_SCAC", StringType(), True),
        StructField("_SaleVoided", StringType(), True),
        StructField("_SearchCriteria1", StringType(), True),
        StructField("_SearchCriteria2", StringType(), True),
        StructField("_SellerOrganizationCode", StringType(), True),
        StructField("_ShipToKey", StringType(), True),
        StructField("_SourceIPAddress", StringType(), True),
        StructField("_SourcingClassification", StringType(), True),
        StructField("_TaxExemptFlag", StringType(), True),
        StructField("_TaxExemptionCertificate", StringType(), True),
        StructField("_TaxJurisdiction", StringType(), True),
        StructField("_TaxPayerId", StringType(), True),
        StructField("_TermsCode", StringType(), True),
        StructField("_TotalAdjustmentAmount", StringType(), True),
        StructField("_isHistory", StringType(), True),
    ]
)

schema_order_return_orders_for_exchange = ArrayType(
    [
        StructType(
            StructField("ReturnOrderForExchange", schema_return_order_for_exchange)
        )
    ]
)

schema_exchange_order_extn = StructType(
    [
        StructField("_CommentsFromStore", StringType(), True),
        StructField("_ExtnChannelOrderNo", StringType(), True),
        StructField("_ExtnEmpID", StringType(), True),
        StructField("_ExtnGSTNo", StringType(), True),
        StructField("_ExtnIRNStatus", StringType(), True),
        StructField("_ExtnInterSoreDocNo", StringType(), True),
        StructField("_ExtnManualOrderReadyForConfirm", StringType(), True),
        StructField("_SaleDate", StringType(), True),
        StructField("_ZECPReason", StringType(), True),
    ]
)

schema_exchange_order = StructType(
    [
        StructField("Extn", schema_exchange_order_extn, True),
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
        StructField("_DocumentType", StringType(), True),
        StructField("_EnterpriseCode", StringType(), True),
        StructField("_OrderNo", StringType(), True),
    ]
)

schema_order_exchange_orders = ArrayType(
    StructType([StructField("ExchangeOrder", schema_exchange_order, True)])
)

schema_order_audit_order = StructType(
    [
        StructField("_DocumentType", StringType(), True),
        StructField("_EnterpriseCode", StringType(), True),
        StructField("_OrderNo", StringType(), True),
    ]
)

schema_order_audit_modification_type = StructType(
    [
        StructField("_Name", StringType(), True),
        StructField("_ScreenName", StringType(), True),
    ]
)

schema_order_audit_level_modification_types = ArrayType(
    StructType([StructField("ModificationType", schema_order_audit_modification_type)])
)

schema_order_audit_level_detail_attribute = StructType(
    [
        StructField("_ModificationType", StringType(), True),
        StructField("_Name", StringType(), True),
        StructField("_NewValue", StringType(), True),
        StructField("_OldValue", StringType(), True),
    ]
)

schema_order_audit_level_detail_attributes = StructType(
    [
        StructField("Attribute", schema_order_audit_level_detail_attribute, True),
    ]
)

schema_order_audit_level_detail = StructType(
    [
        StructField("Attributes", schema_order_audit_level_detail_attributes, True),
        StructField("_Action", StringType(), True),
        StructField("_AuditType", StringType(), True),
    ]
)
schema_order_audit_level_details = ArrayType(
    StructType([StructField("OrderAuditDetail", schema_order_audit_level_detail, True)])
)

schema_order_audit_level = StructType(
    [
        StructField(
            "ModificationTypes", schema_order_audit_level_modification_types, True
        ),
        StructField("OrderAuditDetails", schema_order_audit_level_details, True),
        StructField("OrderLine", StringType(), True),
        StructField("_ModificationLevel", StringType(), True),
        StructField("_ModificationLevelScreenName", StringType(), True),
        StructField("_OrderLineKey", StringType(), True),
        StructField("_OrderReleaseKey", StringType(), True),
    ]
)

schema_order_audit_auditlevels = ArrayType(
    StructType([StructField("OrderAuditLevel", schema_order_audit_level, True)])
)

schema_order_audit = StructType(
    [
        StructField("Order", schema_order_audit_order, True),
        StructField("OrderAuditLevels", schema_order_audit_auditlevels, True),
        StructField("_AuditTransactionId", StringType(), True),
        StructField("_OrderAuditKey", StringType(), True),
        StructField("_OrderHeaderKey", StringType(), True),
        StructField("_ReasonCode", StringType(), True),
        StructField("_ReasonText", StringType(), True),
        StructField("_Reference1", StringType(), True),
        StructField("_Reference2", StringType(), True),
        StructField("_Reference3", StringType(), True),
        StructField("_Reference4", StringType(), True),
        StructField("_XMLFlag", StringType(), True),
    ]
)


schema_order_audits = ArrayType(
    StructType([StructField("Order", schema_order_audit, True)])
)

schema_order_extn = StructType(
    [
        StructField("_CashierID", StringType(), True),
        StructField("_CashierName", StringType(), True),
        StructField("_CommentsFromStore", StringType(), True),
        StructField("_ExtnChannelOrderNo", StringType(), True),
        StructField("_ExtnDty", StringType(), True),
        StructField("_ExtnEmpID", StringType(), True),
        StructField("_ExtnEnableOrderPurge", StringType(), True),
        StructField("_ExtnGSTNo", StringType(), True),
        StructField("_ExtnIRNAckNo", StringType(), True),
        StructField("_ExtnIRNNo", StringType(), True),
        StructField("_ExtnIRNStatus", StringType(), True),
        StructField("_ExtnInterSoreDocNo", StringType(), True),
        StructField("_ExtnManualOrderReadyForConfirm", StringType(), True),
        StructField("_ExtnRetnInvoiceOrderNo", StringType(), True),
        StructField("_ExtnSalesInvoiceOrderDate", StringType(), True),
        StructField("_ExtnSalesInvoiceOrderNo", StringType(), True),
        StructField("_ExtnSalesOrderNo", StringType(), True),
        StructField("_GiftWrappingFlag", StringType(), True),
        StructField("_MaxRepaymentDate", StringType(), True),
        StructField("_RejectedReason", StringType(), True),
        StructField("_SaleDate", StringType(), True),
        StructField("_TillNo", StringType(), True),
        StructField("_ZECPReason", StringType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_order = StructType(
    [
        StructField("AdditionalAddresses", schema_order_additional_addresses, True),
        StructField(
            "ChargeTransactionDetails", schema_order_charge_transaction_details, True
        ),
        StructField("Customer", schema_order_customer, True),
        StructField("Extn", schema_order_extn, True),
        StructField("HeaderCharges", schema_order_header_charges, True),
        StructField("Instructions", schema_order_instructions, True),
        StructField("InvoicedTotals", schema_order_invoiced_totals, True),
        StructField("Notes", schema_order_notes, True),
        StructField("OrderHoldTypes", schema_order_hold_types, True),
        StructField("OrderLines", schema_order_lines, True),
        StructField("OverallTotals", schema_order_overall_totals, True),
        StructField("PaymentMethods", schema_order_payment_methods, True),
        StructField("PersonInfoBillTo", schema_order_person_info_bill_to, True),
        StructField("PersonInfoShipTo", schema_order_person_info_ship_to, True),
        StructField("PriceInfo", schema_order_price_info, True),
        StructField("RemainingTotals", schema_order_remaining_totals, True),
        StructField("Shipments", schema_order_shipments, True),
        StructField(
            "ReturnOrdersForExchange", schema_order_return_orders_for_exchange, True
        ),
        StructField("ExchangeOrders", schema_order_exchange_orders, True),
        StructField("OrderAudits", schema_order_audits, True),
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
        StructField("_ActualPricingDate", StringType(), True),
        StructField("_AdjustmentInvoicePending", StringType(), True),
        StructField("_AllAddressesVerified", StringType(), True),
        StructField("_ApprovalCycle", StringType(), True),
        StructField("_BillToKey", StringType(), True),
        StructField("_ChainType", StringType(), True),
        StructField("_ComplimentaryGiftBoxQty", StringType(), True),
        StructField("_CreatedAtNode", StringType(), True),
        StructField("_Createprogid", StringType(), True),
        StructField("_Createuserid", StringType(), True),
        StructField("_CustCustPONo", StringType(), True),
        StructField("_CustomerAge", StringType(), True),
        StructField("_CustomerFirstName", StringType(), True),
        StructField("_CustomerLastName", StringType(), True),
        StructField("_CustomerPhoneNo", StringType(), True),
        StructField("_CustomerZipCode", StringType(), True),
        StructField("_DoNotConsolidate", StringType(), True),
        StructField("_HasDerivedChild", StringType(), True),
        StructField("_HasDerivedParent", StringType(), True),
        StructField("_InternalApp", StringType(), True),
        StructField("_InvoiceComplete", StringType(), True),
        StructField("_Lockid", StringType(), True),
        StructField("_Modifyprogid", StringType(), True),
        StructField("_Modifyuserid", StringType(), True),
        StructField("_NextAlertTs", StringType(), True),
        StructField("_NoOfAuthStrikes", StringType(), True),
        StructField("_OrderComplete", StringType(), True),
        StructField("_PendingTransferIn", StringType(), True),
        StructField("_PriceOrder", StringType(), True),
        StructField("_PriceProgramName", StringType(), True),
        StructField("_PropagateCancellations", StringType(), True),
        StructField("_ReserveInventoryFlag", StringType(), True),
        StructField("_ReturnByGiftRecipient", StringType(), True),
        StructField("_SaleVoided", StringType(), True),
        StructField("_ShipToKey", StringType(), True),
        StructField("_SourceIPAddress", StringType(), True),
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

schema_sc_status_changes_order_line = StructType(
    [
        StructField("_NewStatus", DoubleType(), True),
        StructField("_NewStatusDate", TimestampType(), True),
        StructField("_OldStatus", DoubleType(), True),
        StructField("_OldStatusDate", TimestampType(), True),
        StructField("_PrimeLineNo", LongType(), True),
        StructField("_Quantity", DoubleType(), True),
        StructField("_SubLineNo", LongType(), True),
        StructField("_VALUE", StringType(), True),
    ]
)

schema_sc_status_changes = ArrayType(
    StructType([StructField("OrderLine", schema_sc_status_changes_order_line, True)])
)

schema_sc_payment_method = StructType(
    [
        StructField("Modifyts", StringType(), True),
        StructField("PaymentKey", StringType(), True),
    ]
)

schema_sc_payment_methods = ArrayType(
    StructType([StructField("PaymentMethod", schema_sc_payment_method, True)])
)

schema_sc_refund_status = StructType(
    [
        StructField("AutoRefundKey", StringType(), True),
        StructField("PrimeLineNo", StringType(), True),
        StructField("RefundStatus", StringType(), True),
        StructField("Statusts", TimestampType(), True),
    ]
)

schema_sc_refund_statuses = ArrayType(
    StructType([StructField("RefundStatus", schema_sc_refund_status, True)])
)

schema_state_changes = StructType(
    [
        StructField("PaymentMethods", schema_sc_payment_methods, True),
        StructField("RefundStatuses", schema_sc_refund_statuses, True),
    ]
)


payload_schema = StructType(
    [
        StructField("EventDetails", schema_event_details, True),
        StructField("CurrentState", schema_current_state, True),
        StructField("StateChanges", schema_state_changes, True),
        StructField("_corrupt_record", StringType(), True),
    ]
)
