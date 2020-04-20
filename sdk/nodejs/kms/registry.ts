// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

export class Registry extends pulumi.CustomResource {
    /**
     * Get an existing Registry resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RegistryState, opts?: pulumi.CustomResourceOptions): Registry {
        return new Registry(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:kms/registry:Registry';

    /**
     * Returns true if the given object is an instance of Registry.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Registry {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Registry.__pulumiType;
    }

    public readonly credentials!: pulumi.Output<outputs.kms.RegistryCredential[] | undefined>;
    public readonly eventNotificationConfigs!: pulumi.Output<outputs.kms.RegistryEventNotificationConfigItem[]>;
    public readonly httpConfig!: pulumi.Output<outputs.kms.RegistryHttpConfig>;
    public readonly logLevel!: pulumi.Output<string | undefined>;
    public readonly mqttConfig!: pulumi.Output<outputs.kms.RegistryMqttConfig>;
    public readonly name!: pulumi.Output<string>;
    public readonly project!: pulumi.Output<string>;
    public readonly region!: pulumi.Output<string>;
    public readonly stateNotificationConfig!: pulumi.Output<outputs.kms.RegistryStateNotificationConfig | undefined>;

    /**
     * Create a Registry resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: RegistryArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RegistryArgs | RegistryState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as RegistryState | undefined;
            inputs["credentials"] = state ? state.credentials : undefined;
            inputs["eventNotificationConfigs"] = state ? state.eventNotificationConfigs : undefined;
            inputs["httpConfig"] = state ? state.httpConfig : undefined;
            inputs["logLevel"] = state ? state.logLevel : undefined;
            inputs["mqttConfig"] = state ? state.mqttConfig : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["stateNotificationConfig"] = state ? state.stateNotificationConfig : undefined;
        } else {
            const args = argsOrState as RegistryArgs | undefined;
            inputs["credentials"] = args ? args.credentials : undefined;
            inputs["eventNotificationConfigs"] = args ? args.eventNotificationConfigs : undefined;
            inputs["httpConfig"] = args ? args.httpConfig : undefined;
            inputs["logLevel"] = args ? args.logLevel : undefined;
            inputs["mqttConfig"] = args ? args.mqttConfig : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["stateNotificationConfig"] = args ? args.stateNotificationConfig : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Registry.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Registry resources.
 */
export interface RegistryState {
    readonly credentials?: pulumi.Input<pulumi.Input<inputs.kms.RegistryCredential>[]>;
    readonly eventNotificationConfigs?: pulumi.Input<pulumi.Input<inputs.kms.RegistryEventNotificationConfigItem>[]>;
    readonly httpConfig?: pulumi.Input<inputs.kms.RegistryHttpConfig>;
    readonly logLevel?: pulumi.Input<string>;
    readonly mqttConfig?: pulumi.Input<inputs.kms.RegistryMqttConfig>;
    readonly name?: pulumi.Input<string>;
    readonly project?: pulumi.Input<string>;
    readonly region?: pulumi.Input<string>;
    readonly stateNotificationConfig?: pulumi.Input<inputs.kms.RegistryStateNotificationConfig>;
}

/**
 * The set of arguments for constructing a Registry resource.
 */
export interface RegistryArgs {
    readonly credentials?: pulumi.Input<pulumi.Input<inputs.kms.RegistryCredential>[]>;
    readonly eventNotificationConfigs?: pulumi.Input<pulumi.Input<inputs.kms.RegistryEventNotificationConfigItem>[]>;
    readonly httpConfig?: pulumi.Input<inputs.kms.RegistryHttpConfig>;
    readonly logLevel?: pulumi.Input<string>;
    readonly mqttConfig?: pulumi.Input<inputs.kms.RegistryMqttConfig>;
    readonly name?: pulumi.Input<string>;
    readonly project?: pulumi.Input<string>;
    readonly region?: pulumi.Input<string>;
    readonly stateNotificationConfig?: pulumi.Input<inputs.kms.RegistryStateNotificationConfig>;
}
