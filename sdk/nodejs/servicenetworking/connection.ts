// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * > **Warning:** This resource is in beta, and should be used with the terraform-provider-google-beta provider.
 * See [Provider Versions](https://terraform.io/docs/providers/google/provider_versions.html) for more details on beta resources.
 * 
 * Manages a private VPC connection with a GCP service provider. For more information see
 * [the official documentation](https://cloud.google.com/vpc/docs/configure-private-services-access#creating-connection)
 * and
 * [API](https://cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services.connections).
 * 
 * ## Example usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const peeringNetwork = new gcp.compute.Network("peering_network", {});
 * const privateIpAlloc = new gcp.compute.GlobalAddress("private_ip_alloc", {
 *     addressType: "INTERNAL",
 *     network: peeringNetwork.selfLink,
 *     prefixLength: 16,
 *     purpose: "VPC_PEERING",
 * });
 * const foobar = new gcp.servicenetworking.Connection("foobar", {
 *     network: peeringNetwork.selfLink,
 *     reservedPeeringRanges: [privateIpAlloc.name],
 *     service: "servicenetworking.googleapis.com",
 * });
 * ```
 */
export class Connection extends pulumi.CustomResource {
    /**
     * Get an existing Connection resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConnectionState, opts?: pulumi.CustomResourceOptions): Connection {
        return new Connection(name, <any>state, { ...opts, id: id });
    }

    /**
     * Name of VPC network connected with service producers using VPC peering.
     */
    public readonly network: pulumi.Output<string>;
    /**
     * Named IP address range(s) of PEERING type reserved for
     * this service provider. Note that invoking this method with a different range when connection
     * is already established will not reallocate already provisioned service producer subnetworks.
     */
    public readonly reservedPeeringRanges: pulumi.Output<string[]>;
    /**
     * Provider peering service that is managing peering connectivity for a
     * service provider organization. For Google services that support this functionality it is
     * 'servicenetworking.googleapis.com'.
     */
    public readonly service: pulumi.Output<string>;

    /**
     * Create a Connection resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ConnectionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ConnectionArgs | ConnectionState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: ConnectionState = argsOrState as ConnectionState | undefined;
            inputs["network"] = state ? state.network : undefined;
            inputs["reservedPeeringRanges"] = state ? state.reservedPeeringRanges : undefined;
            inputs["service"] = state ? state.service : undefined;
        } else {
            const args = argsOrState as ConnectionArgs | undefined;
            if (!args || args.network === undefined) {
                throw new Error("Missing required property 'network'");
            }
            if (!args || args.reservedPeeringRanges === undefined) {
                throw new Error("Missing required property 'reservedPeeringRanges'");
            }
            if (!args || args.service === undefined) {
                throw new Error("Missing required property 'service'");
            }
            inputs["network"] = args ? args.network : undefined;
            inputs["reservedPeeringRanges"] = args ? args.reservedPeeringRanges : undefined;
            inputs["service"] = args ? args.service : undefined;
        }
        super("gcp:servicenetworking/connection:Connection", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Connection resources.
 */
export interface ConnectionState {
    /**
     * Name of VPC network connected with service producers using VPC peering.
     */
    readonly network?: pulumi.Input<string>;
    /**
     * Named IP address range(s) of PEERING type reserved for
     * this service provider. Note that invoking this method with a different range when connection
     * is already established will not reallocate already provisioned service producer subnetworks.
     */
    readonly reservedPeeringRanges?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Provider peering service that is managing peering connectivity for a
     * service provider organization. For Google services that support this functionality it is
     * 'servicenetworking.googleapis.com'.
     */
    readonly service?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Connection resource.
 */
export interface ConnectionArgs {
    /**
     * Name of VPC network connected with service producers using VPC peering.
     */
    readonly network: pulumi.Input<string>;
    /**
     * Named IP address range(s) of PEERING type reserved for
     * this service provider. Note that invoking this method with a different range when connection
     * is already established will not reallocate already provisioned service producer subnetworks.
     */
    readonly reservedPeeringRanges: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Provider peering service that is managing peering connectivity for a
     * service provider organization. For Google services that support this functionality it is
     * 'servicenetworking.googleapis.com'.
     */
    readonly service: pulumi.Input<string>;
}
