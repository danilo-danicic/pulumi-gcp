// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * A NotificationChannel is a medium through which an alert is delivered
 * when a policy violation is detected. Examples of channels include email, SMS,
 * and third-party messaging applications. Fields containing sensitive information
 * like authentication tokens or contact info are only partially populated on retrieval.
 * 
 * 
 * To get more information about NotificationChannel, see:
 * 
 * * [API documentation](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels)
 * * How-to Guides
 *     * [Official Documentation](https://cloud.google.com/monitoring/api/v3/)
 * 
 * ## Example Usage - Notification Channel Basic
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const basic = new gcp.monitoring.NotificationChannel("basic", {
 *     displayName: "Test Notification Channel",
 *     labels: {
 *         email_address: "fake_email@blahblah.com",
 *     },
 *     type: "email",
 * });
 * ```
 */
export class NotificationChannel extends pulumi.CustomResource {
    /**
     * Get an existing NotificationChannel resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NotificationChannelState, opts?: pulumi.CustomResourceOptions): NotificationChannel {
        return new NotificationChannel(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:monitoring/notificationChannel:NotificationChannel';

    /**
     * Returns true if the given object is an instance of NotificationChannel.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is NotificationChannel {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === NotificationChannel.__pulumiType;
    }

    public readonly description!: pulumi.Output<string | undefined>;
    public readonly displayName!: pulumi.Output<string>;
    public readonly enabled!: pulumi.Output<boolean | undefined>;
    public readonly labels!: pulumi.Output<{[key: string]: string} | undefined>;
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    public readonly type!: pulumi.Output<string>;
    public readonly userLabels!: pulumi.Output<{[key: string]: string} | undefined>;
    public /*out*/ readonly verificationStatus!: pulumi.Output<string>;

    /**
     * Create a NotificationChannel resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NotificationChannelArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: NotificationChannelArgs | NotificationChannelState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as NotificationChannelState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["displayName"] = state ? state.displayName : undefined;
            inputs["enabled"] = state ? state.enabled : undefined;
            inputs["labels"] = state ? state.labels : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["type"] = state ? state.type : undefined;
            inputs["userLabels"] = state ? state.userLabels : undefined;
            inputs["verificationStatus"] = state ? state.verificationStatus : undefined;
        } else {
            const args = argsOrState as NotificationChannelArgs | undefined;
            if (!args || args.displayName === undefined) {
                throw new Error("Missing required property 'displayName'");
            }
            if (!args || args.type === undefined) {
                throw new Error("Missing required property 'type'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["displayName"] = args ? args.displayName : undefined;
            inputs["enabled"] = args ? args.enabled : undefined;
            inputs["labels"] = args ? args.labels : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["type"] = args ? args.type : undefined;
            inputs["userLabels"] = args ? args.userLabels : undefined;
            inputs["name"] = undefined /*out*/;
            inputs["verificationStatus"] = undefined /*out*/;
        }
        super(NotificationChannel.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering NotificationChannel resources.
 */
export interface NotificationChannelState {
    readonly description?: pulumi.Input<string>;
    readonly displayName?: pulumi.Input<string>;
    readonly enabled?: pulumi.Input<boolean>;
    readonly labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    readonly type?: pulumi.Input<string>;
    readonly userLabels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    readonly verificationStatus?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a NotificationChannel resource.
 */
export interface NotificationChannelArgs {
    readonly description?: pulumi.Input<string>;
    readonly displayName: pulumi.Input<string>;
    readonly enabled?: pulumi.Input<boolean>;
    readonly labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    readonly type: pulumi.Input<string>;
    readonly userLabels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}
