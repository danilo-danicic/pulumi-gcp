// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

export class Gateway extends pulumi.CustomResource {
    /**
     * Get an existing Gateway resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GatewayState, opts?: pulumi.CustomResourceOptions): Gateway {
        return new Gateway(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:apigateway/gateway:Gateway';

    /**
     * Returns true if the given object is an instance of Gateway.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Gateway {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Gateway.__pulumiType;
    }

    /**
     * Resource name of the API Config for this Gateway. Format: projects/{project}/locations/global/apis/{api}/configs/{apiConfig}
     */
    public readonly apiConfig!: pulumi.Output<string>;
    /**
     * The default API Gateway host name of the form {gatewayId}-{hash}.{region_code}.gateway.dev.
     */
    public /*out*/ readonly defaultHostname!: pulumi.Output<string>;
    /**
     * A user-visible name for the API.
     */
    public readonly displayName!: pulumi.Output<string>;
    /**
     * Identifier to assign to the Gateway. Must be unique within scope of the parent resource(project).
     */
    public readonly gatewayId!: pulumi.Output<string>;
    /**
     * Resource labels to represent user-provided metadata.
     */
    public readonly labels!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * Resource name of the Gateway. Format: projects/{project}/locations/{region}/gateways/{gateway}
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * The region of the gateway for the API.
     */
    public readonly region!: pulumi.Output<string>;

    /**
     * Create a Gateway resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GatewayArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GatewayArgs | GatewayState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as GatewayState | undefined;
            inputs["apiConfig"] = state ? state.apiConfig : undefined;
            inputs["defaultHostname"] = state ? state.defaultHostname : undefined;
            inputs["displayName"] = state ? state.displayName : undefined;
            inputs["gatewayId"] = state ? state.gatewayId : undefined;
            inputs["labels"] = state ? state.labels : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["region"] = state ? state.region : undefined;
        } else {
            const args = argsOrState as GatewayArgs | undefined;
            if (!args || args.apiConfig === undefined) {
                throw new Error("Missing required property 'apiConfig'");
            }
            if (!args || args.gatewayId === undefined) {
                throw new Error("Missing required property 'gatewayId'");
            }
            inputs["apiConfig"] = args ? args.apiConfig : undefined;
            inputs["displayName"] = args ? args.displayName : undefined;
            inputs["gatewayId"] = args ? args.gatewayId : undefined;
            inputs["labels"] = args ? args.labels : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["defaultHostname"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Gateway.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Gateway resources.
 */
export interface GatewayState {
    /**
     * Resource name of the API Config for this Gateway. Format: projects/{project}/locations/global/apis/{api}/configs/{apiConfig}
     */
    readonly apiConfig?: pulumi.Input<string>;
    /**
     * The default API Gateway host name of the form {gatewayId}-{hash}.{region_code}.gateway.dev.
     */
    readonly defaultHostname?: pulumi.Input<string>;
    /**
     * A user-visible name for the API.
     */
    readonly displayName?: pulumi.Input<string>;
    /**
     * Identifier to assign to the Gateway. Must be unique within scope of the parent resource(project).
     */
    readonly gatewayId?: pulumi.Input<string>;
    /**
     * Resource labels to represent user-provided metadata.
     */
    readonly labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Resource name of the Gateway. Format: projects/{project}/locations/{region}/gateways/{gateway}
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The region of the gateway for the API.
     */
    readonly region?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Gateway resource.
 */
export interface GatewayArgs {
    /**
     * Resource name of the API Config for this Gateway. Format: projects/{project}/locations/global/apis/{api}/configs/{apiConfig}
     */
    readonly apiConfig: pulumi.Input<string>;
    /**
     * A user-visible name for the API.
     */
    readonly displayName?: pulumi.Input<string>;
    /**
     * Identifier to assign to the Gateway. Must be unique within scope of the parent resource(project).
     */
    readonly gatewayId: pulumi.Input<string>;
    /**
     * Resource labels to represent user-provided metadata.
     */
    readonly labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The region of the gateway for the API.
     */
    readonly region?: pulumi.Input<string>;
}