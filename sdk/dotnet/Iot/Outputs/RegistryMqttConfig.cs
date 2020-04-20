// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Iot.Outputs
{

    [OutputType]
    public sealed class RegistryMqttConfig
    {
        /// <summary>
        /// The field allows `MQTT_ENABLED` or `MQTT_DISABLED`.
        /// </summary>
        public readonly string MqttEnabledState;

        [OutputConstructor]
        private RegistryMqttConfig(string mqttEnabledState)
        {
            MqttEnabledState = mqttEnabledState;
        }
    }
}
