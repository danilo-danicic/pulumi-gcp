// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iot

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// A Google Cloud IoT Core device registry.
//
// To get more information about DeviceRegistry, see:
//
// * [API documentation](https://cloud.google.com/iot/docs/reference/cloudiot/rest/)
// * How-to Guides
//     * [Official Documentation](https://cloud.google.com/iot/docs/)
//
// ## Example Usage
type Registry struct {
	pulumi.CustomResourceState

	// List of public key certificates to authenticate devices.
	// The structure is documented below.
	Credentials RegistryCredentialArrayOutput `pulumi:"credentials"`
	// List of configurations for event notifications, such as PubSub topics
	// to publish device events to.
	// Structure is documented below.
	EventNotificationConfigs RegistryEventNotificationConfigItemArrayOutput `pulumi:"eventNotificationConfigs"`
	// Activate or deactivate HTTP.
	// The structure is documented below.
	HttpConfig pulumi.MapOutput `pulumi:"httpConfig"`
	// The default logging verbosity for activity from devices in this
	// registry. Specifies which events should be written to logs. For
	// example, if the LogLevel is ERROR, only events that terminate in
	// errors will be logged. LogLevel is inclusive; enabling INFO logging
	// will also enable ERROR logging.
	// Default value is `NONE`.
	// Possible values are `NONE`, `ERROR`, `INFO`, and `DEBUG`.
	LogLevel pulumi.StringPtrOutput `pulumi:"logLevel"`
	// Activate or deactivate MQTT.
	// The structure is documented below.
	MqttConfig pulumi.MapOutput `pulumi:"mqttConfig"`
	// A unique name for the resource, required by device registry.
	Name pulumi.StringOutput `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// The region in which the created registry should reside.
	// If it is not provided, the provider region is used.
	Region pulumi.StringOutput `pulumi:"region"`
	// A PubSub topic to publish device state updates.
	// The structure is documented below.
	StateNotificationConfig pulumi.MapOutput `pulumi:"stateNotificationConfig"`
}

// NewRegistry registers a new resource with the given unique name, arguments, and options.
func NewRegistry(ctx *pulumi.Context,
	name string, args *RegistryArgs, opts ...pulumi.ResourceOption) (*Registry, error) {
	if args == nil {
		args = &RegistryArgs{}
	}
	aliases := pulumi.Aliases([]pulumi.Alias{
		{
			Type: pulumi.String("gcp:kms/registry:Registry"),
		},
	})
	opts = append(opts, aliases)
	var resource Registry
	err := ctx.RegisterResource("gcp:iot/registry:Registry", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRegistry gets an existing Registry resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRegistry(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RegistryState, opts ...pulumi.ResourceOption) (*Registry, error) {
	var resource Registry
	err := ctx.ReadResource("gcp:iot/registry:Registry", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Registry resources.
type registryState struct {
	// List of public key certificates to authenticate devices.
	// The structure is documented below.
	Credentials []RegistryCredential `pulumi:"credentials"`
	// List of configurations for event notifications, such as PubSub topics
	// to publish device events to.
	// Structure is documented below.
	EventNotificationConfigs []RegistryEventNotificationConfigItem `pulumi:"eventNotificationConfigs"`
	// Activate or deactivate HTTP.
	// The structure is documented below.
	HttpConfig map[string]interface{} `pulumi:"httpConfig"`
	// The default logging verbosity for activity from devices in this
	// registry. Specifies which events should be written to logs. For
	// example, if the LogLevel is ERROR, only events that terminate in
	// errors will be logged. LogLevel is inclusive; enabling INFO logging
	// will also enable ERROR logging.
	// Default value is `NONE`.
	// Possible values are `NONE`, `ERROR`, `INFO`, and `DEBUG`.
	LogLevel *string `pulumi:"logLevel"`
	// Activate or deactivate MQTT.
	// The structure is documented below.
	MqttConfig map[string]interface{} `pulumi:"mqttConfig"`
	// A unique name for the resource, required by device registry.
	Name *string `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The region in which the created registry should reside.
	// If it is not provided, the provider region is used.
	Region *string `pulumi:"region"`
	// A PubSub topic to publish device state updates.
	// The structure is documented below.
	StateNotificationConfig map[string]interface{} `pulumi:"stateNotificationConfig"`
}

type RegistryState struct {
	// List of public key certificates to authenticate devices.
	// The structure is documented below.
	Credentials RegistryCredentialArrayInput
	// List of configurations for event notifications, such as PubSub topics
	// to publish device events to.
	// Structure is documented below.
	EventNotificationConfigs RegistryEventNotificationConfigItemArrayInput
	// Activate or deactivate HTTP.
	// The structure is documented below.
	HttpConfig pulumi.MapInput
	// The default logging verbosity for activity from devices in this
	// registry. Specifies which events should be written to logs. For
	// example, if the LogLevel is ERROR, only events that terminate in
	// errors will be logged. LogLevel is inclusive; enabling INFO logging
	// will also enable ERROR logging.
	// Default value is `NONE`.
	// Possible values are `NONE`, `ERROR`, `INFO`, and `DEBUG`.
	LogLevel pulumi.StringPtrInput
	// Activate or deactivate MQTT.
	// The structure is documented below.
	MqttConfig pulumi.MapInput
	// A unique name for the resource, required by device registry.
	Name pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// The region in which the created registry should reside.
	// If it is not provided, the provider region is used.
	Region pulumi.StringPtrInput
	// A PubSub topic to publish device state updates.
	// The structure is documented below.
	StateNotificationConfig pulumi.MapInput
}

func (RegistryState) ElementType() reflect.Type {
	return reflect.TypeOf((*registryState)(nil)).Elem()
}

type registryArgs struct {
	// List of public key certificates to authenticate devices.
	// The structure is documented below.
	Credentials []RegistryCredential `pulumi:"credentials"`
	// List of configurations for event notifications, such as PubSub topics
	// to publish device events to.
	// Structure is documented below.
	EventNotificationConfigs []RegistryEventNotificationConfigItem `pulumi:"eventNotificationConfigs"`
	// Activate or deactivate HTTP.
	// The structure is documented below.
	HttpConfig map[string]interface{} `pulumi:"httpConfig"`
	// The default logging verbosity for activity from devices in this
	// registry. Specifies which events should be written to logs. For
	// example, if the LogLevel is ERROR, only events that terminate in
	// errors will be logged. LogLevel is inclusive; enabling INFO logging
	// will also enable ERROR logging.
	// Default value is `NONE`.
	// Possible values are `NONE`, `ERROR`, `INFO`, and `DEBUG`.
	LogLevel *string `pulumi:"logLevel"`
	// Activate or deactivate MQTT.
	// The structure is documented below.
	MqttConfig map[string]interface{} `pulumi:"mqttConfig"`
	// A unique name for the resource, required by device registry.
	Name *string `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The region in which the created registry should reside.
	// If it is not provided, the provider region is used.
	Region *string `pulumi:"region"`
	// A PubSub topic to publish device state updates.
	// The structure is documented below.
	StateNotificationConfig map[string]interface{} `pulumi:"stateNotificationConfig"`
}

// The set of arguments for constructing a Registry resource.
type RegistryArgs struct {
	// List of public key certificates to authenticate devices.
	// The structure is documented below.
	Credentials RegistryCredentialArrayInput
	// List of configurations for event notifications, such as PubSub topics
	// to publish device events to.
	// Structure is documented below.
	EventNotificationConfigs RegistryEventNotificationConfigItemArrayInput
	// Activate or deactivate HTTP.
	// The structure is documented below.
	HttpConfig pulumi.MapInput
	// The default logging verbosity for activity from devices in this
	// registry. Specifies which events should be written to logs. For
	// example, if the LogLevel is ERROR, only events that terminate in
	// errors will be logged. LogLevel is inclusive; enabling INFO logging
	// will also enable ERROR logging.
	// Default value is `NONE`.
	// Possible values are `NONE`, `ERROR`, `INFO`, and `DEBUG`.
	LogLevel pulumi.StringPtrInput
	// Activate or deactivate MQTT.
	// The structure is documented below.
	MqttConfig pulumi.MapInput
	// A unique name for the resource, required by device registry.
	Name pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// The region in which the created registry should reside.
	// If it is not provided, the provider region is used.
	Region pulumi.StringPtrInput
	// A PubSub topic to publish device state updates.
	// The structure is documented below.
	StateNotificationConfig pulumi.MapInput
}

func (RegistryArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*registryArgs)(nil)).Elem()
}
