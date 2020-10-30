// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Billing.Inputs
{

    public sealed class BudgetAllUpdatesRuleArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Boolean. When set to true, disables default notifications sent
        /// when a threshold is exceeded. Default recipients are
        /// those with Billing Account Administrators and Billing
        /// Account Users IAM roles for the target account.
        /// </summary>
        [Input("disableDefaultIamRecipients")]
        public Input<bool>? DisableDefaultIamRecipients { get; set; }

        [Input("monitoringNotificationChannels")]
        private InputList<string>? _monitoringNotificationChannels;

        /// <summary>
        /// The full resource name of a monitoring notification
        /// channel in the form
        /// projects/{project_id}/notificationChannels/{channel_id}.
        /// A maximum of 5 channels are allowed.
        /// </summary>
        public InputList<string> MonitoringNotificationChannels
        {
            get => _monitoringNotificationChannels ?? (_monitoringNotificationChannels = new InputList<string>());
            set => _monitoringNotificationChannels = value;
        }

        /// <summary>
        /// The name of the Cloud Pub/Sub topic where budget related
        /// messages will be published, in the form
        /// projects/{project_id}/topics/{topic_id}. Updates are sent
        /// at regular intervals to the topic.
        /// </summary>
        [Input("pubsubTopic")]
        public Input<string>? PubsubTopic { get; set; }

        /// <summary>
        /// The schema version of the notification. Only "1.0" is
        /// accepted. It represents the JSON schema as defined in
        /// https://cloud.google.com/billing/docs/how-to/budgets#notification_format.
        /// </summary>
        [Input("schemaVersion")]
        public Input<string>? SchemaVersion { get; set; }

        public BudgetAllUpdatesRuleArgs()
        {
        }
    }
}
