# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'AccountIamBindingConditionArgs',
    'AccountIamMemberConditionArgs',
    'BudgetAllUpdatesRuleArgs',
    'BudgetAmountArgs',
    'BudgetAmountSpecifiedAmountArgs',
    'BudgetBudgetFilterArgs',
    'BudgetThresholdRuleArgs',
]

@pulumi.input_type
class AccountIamBindingConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class AccountIamMemberConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class BudgetAllUpdatesRuleArgs:
    def __init__(__self__, *,
                 disable_default_iam_recipients: Optional[pulumi.Input[bool]] = None,
                 monitoring_notification_channels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 pubsub_topic: Optional[pulumi.Input[str]] = None,
                 schema_version: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] disable_default_iam_recipients: Boolean. When set to true, disables default notifications sent
               when a threshold is exceeded. Default recipients are
               those with Billing Account Administrators and Billing
               Account Users IAM roles for the target account.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] monitoring_notification_channels: The full resource name of a monitoring notification
               channel in the form
               projects/{project_id}/notificationChannels/{channel_id}.
               A maximum of 5 channels are allowed.
        :param pulumi.Input[str] pubsub_topic: The name of the Cloud Pub/Sub topic where budget related
               messages will be published, in the form
               projects/{project_id}/topics/{topic_id}. Updates are sent
               at regular intervals to the topic.
        :param pulumi.Input[str] schema_version: The schema version of the notification. Only "1.0" is
               accepted. It represents the JSON schema as defined in
               https://cloud.google.com/billing/docs/how-to/budgets#notification_format.
        """
        if disable_default_iam_recipients is not None:
            pulumi.set(__self__, "disable_default_iam_recipients", disable_default_iam_recipients)
        if monitoring_notification_channels is not None:
            pulumi.set(__self__, "monitoring_notification_channels", monitoring_notification_channels)
        if pubsub_topic is not None:
            pulumi.set(__self__, "pubsub_topic", pubsub_topic)
        if schema_version is not None:
            pulumi.set(__self__, "schema_version", schema_version)

    @property
    @pulumi.getter(name="disableDefaultIamRecipients")
    def disable_default_iam_recipients(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean. When set to true, disables default notifications sent
        when a threshold is exceeded. Default recipients are
        those with Billing Account Administrators and Billing
        Account Users IAM roles for the target account.
        """
        return pulumi.get(self, "disable_default_iam_recipients")

    @disable_default_iam_recipients.setter
    def disable_default_iam_recipients(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_default_iam_recipients", value)

    @property
    @pulumi.getter(name="monitoringNotificationChannels")
    def monitoring_notification_channels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The full resource name of a monitoring notification
        channel in the form
        projects/{project_id}/notificationChannels/{channel_id}.
        A maximum of 5 channels are allowed.
        """
        return pulumi.get(self, "monitoring_notification_channels")

    @monitoring_notification_channels.setter
    def monitoring_notification_channels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "monitoring_notification_channels", value)

    @property
    @pulumi.getter(name="pubsubTopic")
    def pubsub_topic(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Cloud Pub/Sub topic where budget related
        messages will be published, in the form
        projects/{project_id}/topics/{topic_id}. Updates are sent
        at regular intervals to the topic.
        """
        return pulumi.get(self, "pubsub_topic")

    @pubsub_topic.setter
    def pubsub_topic(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pubsub_topic", value)

    @property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> Optional[pulumi.Input[str]]:
        """
        The schema version of the notification. Only "1.0" is
        accepted. It represents the JSON schema as defined in
        https://cloud.google.com/billing/docs/how-to/budgets#notification_format.
        """
        return pulumi.get(self, "schema_version")

    @schema_version.setter
    def schema_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema_version", value)


@pulumi.input_type
class BudgetAmountArgs:
    def __init__(__self__, *,
                 last_period_amount: Optional[pulumi.Input[bool]] = None,
                 specified_amount: Optional[pulumi.Input['BudgetAmountSpecifiedAmountArgs']] = None):
        """
        :param pulumi.Input[bool] last_period_amount: Configures a budget amount that is automatically set to 100% of
               last period's spend.
               Boolean. Set value to true to use. Do not set to false, instead
               use the `specified_amount` block.
        :param pulumi.Input['BudgetAmountSpecifiedAmountArgs'] specified_amount: A specified amount to use as the budget. currencyCode is
               optional. If specified, it must match the currency of the
               billing account. The currencyCode is provided on output.
               Structure is documented below.
        """
        if last_period_amount is not None:
            pulumi.set(__self__, "last_period_amount", last_period_amount)
        if specified_amount is not None:
            pulumi.set(__self__, "specified_amount", specified_amount)

    @property
    @pulumi.getter(name="lastPeriodAmount")
    def last_period_amount(self) -> Optional[pulumi.Input[bool]]:
        """
        Configures a budget amount that is automatically set to 100% of
        last period's spend.
        Boolean. Set value to true to use. Do not set to false, instead
        use the `specified_amount` block.
        """
        return pulumi.get(self, "last_period_amount")

    @last_period_amount.setter
    def last_period_amount(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "last_period_amount", value)

    @property
    @pulumi.getter(name="specifiedAmount")
    def specified_amount(self) -> Optional[pulumi.Input['BudgetAmountSpecifiedAmountArgs']]:
        """
        A specified amount to use as the budget. currencyCode is
        optional. If specified, it must match the currency of the
        billing account. The currencyCode is provided on output.
        Structure is documented below.
        """
        return pulumi.get(self, "specified_amount")

    @specified_amount.setter
    def specified_amount(self, value: Optional[pulumi.Input['BudgetAmountSpecifiedAmountArgs']]):
        pulumi.set(self, "specified_amount", value)


@pulumi.input_type
class BudgetAmountSpecifiedAmountArgs:
    def __init__(__self__, *,
                 currency_code: Optional[pulumi.Input[str]] = None,
                 nanos: Optional[pulumi.Input[int]] = None,
                 units: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] currency_code: The 3-letter currency code defined in ISO 4217.
        :param pulumi.Input[int] nanos: Number of nano (10^-9) units of the amount.
               The value must be between -999,999,999 and +999,999,999
               inclusive. If units is positive, nanos must be positive or
               zero. If units is zero, nanos can be positive, zero, or
               negative. If units is negative, nanos must be negative or
               zero. For example $-1.75 is represented as units=-1 and
               nanos=-750,000,000.
        :param pulumi.Input[str] units: The whole units of the amount. For example if currencyCode
               is "USD", then 1 unit is one US dollar.
        """
        if currency_code is not None:
            pulumi.set(__self__, "currency_code", currency_code)
        if nanos is not None:
            pulumi.set(__self__, "nanos", nanos)
        if units is not None:
            pulumi.set(__self__, "units", units)

    @property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> Optional[pulumi.Input[str]]:
        """
        The 3-letter currency code defined in ISO 4217.
        """
        return pulumi.get(self, "currency_code")

    @currency_code.setter
    def currency_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "currency_code", value)

    @property
    @pulumi.getter
    def nanos(self) -> Optional[pulumi.Input[int]]:
        """
        Number of nano (10^-9) units of the amount.
        The value must be between -999,999,999 and +999,999,999
        inclusive. If units is positive, nanos must be positive or
        zero. If units is zero, nanos can be positive, zero, or
        negative. If units is negative, nanos must be negative or
        zero. For example $-1.75 is represented as units=-1 and
        nanos=-750,000,000.
        """
        return pulumi.get(self, "nanos")

    @nanos.setter
    def nanos(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "nanos", value)

    @property
    @pulumi.getter
    def units(self) -> Optional[pulumi.Input[str]]:
        """
        The whole units of the amount. For example if currencyCode
        is "USD", then 1 unit is one US dollar.
        """
        return pulumi.get(self, "units")

    @units.setter
    def units(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "units", value)


@pulumi.input_type
class BudgetBudgetFilterArgs:
    def __init__(__self__, *,
                 credit_types_treatment: Optional[pulumi.Input[str]] = None,
                 projects: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 services: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] credit_types_treatment: Specifies how credits should be treated when determining spend
               for threshold calculations.
               Default value is `INCLUDE_ALL_CREDITS`.
               Possible values are `INCLUDE_ALL_CREDITS` and `EXCLUDE_ALL_CREDITS`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] projects: A set of projects of the form projects/{project_id},
               specifying that usage from only this set of projects should be
               included in the budget. If omitted, the report will include
               all usage for the billing account, regardless of which project
               the usage occurred on. Only zero or one project can be
               specified currently.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] services: A set of services of the form services/{service_id},
               specifying that usage from only this set of services should be
               included in the budget. If omitted, the report will include
               usage for all the services. The service names are available
               through the Catalog API:
               https://cloud.google.com/billing/v1/how-tos/catalog-api.
        """
        if credit_types_treatment is not None:
            pulumi.set(__self__, "credit_types_treatment", credit_types_treatment)
        if projects is not None:
            pulumi.set(__self__, "projects", projects)
        if services is not None:
            pulumi.set(__self__, "services", services)

    @property
    @pulumi.getter(name="creditTypesTreatment")
    def credit_types_treatment(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies how credits should be treated when determining spend
        for threshold calculations.
        Default value is `INCLUDE_ALL_CREDITS`.
        Possible values are `INCLUDE_ALL_CREDITS` and `EXCLUDE_ALL_CREDITS`.
        """
        return pulumi.get(self, "credit_types_treatment")

    @credit_types_treatment.setter
    def credit_types_treatment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "credit_types_treatment", value)

    @property
    @pulumi.getter
    def projects(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A set of projects of the form projects/{project_id},
        specifying that usage from only this set of projects should be
        included in the budget. If omitted, the report will include
        all usage for the billing account, regardless of which project
        the usage occurred on. Only zero or one project can be
        specified currently.
        """
        return pulumi.get(self, "projects")

    @projects.setter
    def projects(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "projects", value)

    @property
    @pulumi.getter
    def services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A set of services of the form services/{service_id},
        specifying that usage from only this set of services should be
        included in the budget. If omitted, the report will include
        usage for all the services. The service names are available
        through the Catalog API:
        https://cloud.google.com/billing/v1/how-tos/catalog-api.
        """
        return pulumi.get(self, "services")

    @services.setter
    def services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "services", value)


@pulumi.input_type
class BudgetThresholdRuleArgs:
    def __init__(__self__, *,
                 threshold_percent: pulumi.Input[float],
                 spend_basis: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[float] threshold_percent: Send an alert when this threshold is exceeded. This is a
               1.0-based percentage, so 0.5 = 50%. Must be >= 0.
        :param pulumi.Input[str] spend_basis: The type of basis used to determine if spend has passed
               the threshold.
               Default value is `CURRENT_SPEND`.
               Possible values are `CURRENT_SPEND` and `FORECASTED_SPEND`.
        """
        pulumi.set(__self__, "threshold_percent", threshold_percent)
        if spend_basis is not None:
            pulumi.set(__self__, "spend_basis", spend_basis)

    @property
    @pulumi.getter(name="thresholdPercent")
    def threshold_percent(self) -> pulumi.Input[float]:
        """
        Send an alert when this threshold is exceeded. This is a
        1.0-based percentage, so 0.5 = 50%. Must be >= 0.
        """
        return pulumi.get(self, "threshold_percent")

    @threshold_percent.setter
    def threshold_percent(self, value: pulumi.Input[float]):
        pulumi.set(self, "threshold_percent", value)

    @property
    @pulumi.getter(name="spendBasis")
    def spend_basis(self) -> Optional[pulumi.Input[str]]:
        """
        The type of basis used to determine if spend has passed
        the threshold.
        Default value is `CURRENT_SPEND`.
        Possible values are `CURRENT_SPEND` and `FORECASTED_SPEND`.
        """
        return pulumi.get(self, "spend_basis")

    @spend_basis.setter
    def spend_basis(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "spend_basis", value)


