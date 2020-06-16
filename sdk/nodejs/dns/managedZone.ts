// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * A zone is a subtree of the DNS namespace under one administrative
 * responsibility. A ManagedZone is a resource that represents a DNS zone
 * hosted by the Cloud DNS service.
 *
 *
 * To get more information about ManagedZone, see:
 *
 * * [API documentation](https://cloud.google.com/dns/api/v1/managedZones)
 * * How-to Guides
 *     * [Managing Zones](https://cloud.google.com/dns/zones/)
 *
 * ## Example Usage
 *
 * ### Dns Managed Zone Basic
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 *
 * const example_zone = new gcp.dns.ManagedZone("example-zone", {
 *     description: "Example DNS zone",
 *     dnsName: "my-domain.com.",
 *     labels: {
 *         foo: "bar",
 *     },
 * });
 * ```
 *
 * ### Dns Managed Zone Private
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 *
 * const network_1 = new gcp.compute.Network("network-1", {autoCreateSubnetworks: false});
 * const network_2 = new gcp.compute.Network("network-2", {autoCreateSubnetworks: false});
 * const private_zone = new gcp.dns.ManagedZone("private-zone", {
 *     dnsName: "private.example.com.",
 *     description: "Example private DNS zone",
 *     labels: {
 *         foo: "bar",
 *     },
 *     visibility: "private",
 *     private_visibility_config: {
 *         networks: [
 *             {
 *                 networkUrl: network_1.id,
 *             },
 *             {
 *                 networkUrl: network_2.id,
 *             },
 *         ],
 *     },
 * });
 * ```
 *
 * ### Dns Managed Zone Private Forwarding
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 *
 * const network_1 = new gcp.compute.Network("network-1", {autoCreateSubnetworks: false});
 * const network_2 = new gcp.compute.Network("network-2", {autoCreateSubnetworks: false});
 * const private_zone = new gcp.dns.ManagedZone("private-zone", {
 *     dnsName: "private.example.com.",
 *     description: "Example private DNS zone",
 *     labels: {
 *         foo: "bar",
 *     },
 *     visibility: "private",
 *     private_visibility_config: {
 *         networks: [
 *             {
 *                 networkUrl: network_1.selfLink,
 *             },
 *             {
 *                 networkUrl: network_2.selfLink,
 *             },
 *         ],
 *     },
 *     forwarding_config: {
 *         target_name_servers: [
 *             {
 *                 ipv4Address: "172.16.1.10",
 *             },
 *             {
 *                 ipv4Address: "172.16.1.20",
 *             },
 *         ],
 *     },
 * });
 * ```
 *
 * ### Dns Managed Zone Private Peering
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 *
 * const network_source = new gcp.compute.Network("network-source", {autoCreateSubnetworks: false});
 * const network_target = new gcp.compute.Network("network-target", {autoCreateSubnetworks: false});
 * const peering_zone = new gcp.dns.ManagedZone("peering-zone", {
 *     dnsName: "peering.example.com.",
 *     description: "Example private DNS peering zone",
 *     visibility: "private",
 *     private_visibility_config: {
 *         networks: [{
 *             networkUrl: network_source.id,
 *         }],
 *     },
 *     peering_config: {
 *         target_network: {
 *             networkUrl: network_target.id,
 *         },
 *     },
 * });
 * ```
 *
 * ### Dns Managed Zone Service Directory
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 *
 * const example = new gcp.servicedirectory.Namespace("example", {
 *     namespaceId: "example",
 *     location: "us-central1",
 * });
 * const sd_zone = new gcp.dns.ManagedZone("sd-zone", {
 *     dnsName: "services.example.com.",
 *     description: "Example private DNS Service Directory zone",
 *     visibility: "private",
 *     service_directory_config: {
 *         namespace: {
 *             namespaceUrl: example.id,
 *         },
 *     },
 * });
 * const network = new gcp.compute.Network("network", {autoCreateSubnetworks: false});
 * ```
 */
export class ManagedZone extends pulumi.CustomResource {
    /**
     * Get an existing ManagedZone resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ManagedZoneState, opts?: pulumi.CustomResourceOptions): ManagedZone {
        return new ManagedZone(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:dns/managedZone:ManagedZone';

    /**
     * Returns true if the given object is an instance of ManagedZone.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ManagedZone {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ManagedZone.__pulumiType;
    }

    /**
     * A textual description field. Defaults to 'Managed by Pulumi'.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * The DNS name of this managed zone, for instance "example.com.".
     */
    public readonly dnsName!: pulumi.Output<string>;
    /**
     * DNSSEC configuration  Structure is documented below.
     */
    public readonly dnssecConfig!: pulumi.Output<outputs.dns.ManagedZoneDnssecConfig | undefined>;
    /**
     * The presence for this field indicates that outbound forwarding is enabled
     * for this zone. The value of this field contains the set of destinations
     * to forward to.  Structure is documented below.
     */
    public readonly forwardingConfig!: pulumi.Output<outputs.dns.ManagedZoneForwardingConfig | undefined>;
    /**
     * A set of key/value label pairs to assign to this ManagedZone.
     */
    public readonly labels!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * User assigned name for this resource.
     * Must be unique within the project.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Delegate your managed_zone to these virtual name servers; defined by the server
     */
    public /*out*/ readonly nameServers!: pulumi.Output<string[]>;
    /**
     * The presence of this field indicates that DNS Peering is enabled for this
     * zone. The value of this field contains the network to peer with.  Structure is documented below.
     */
    public readonly peeringConfig!: pulumi.Output<outputs.dns.ManagedZonePeeringConfig | undefined>;
    /**
     * For privately visible zones, the set of Virtual Private Cloud
     * resources that the zone is visible from.  Structure is documented below.
     */
    public readonly privateVisibilityConfig!: pulumi.Output<outputs.dns.ManagedZonePrivateVisibilityConfig | undefined>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * Specifies if this is a managed reverse lookup zone. If true, Cloud DNS will resolve reverse
     * lookup queries using automatically configured records for VPC resources. This only applies
     * to networks listed under `privateVisibilityConfig`.
     */
    public readonly reverseLookup!: pulumi.Output<boolean | undefined>;
    /**
     * The presence of this field indicates that this zone is backed by Service Directory. The value of this field contains information related to the namespace associated with the zone.  Structure is documented below.
     */
    public readonly serviceDirectoryConfig!: pulumi.Output<outputs.dns.ManagedZoneServiceDirectoryConfig | undefined>;
    /**
     * The zone's visibility: public zones are exposed to the Internet,
     * while private zones are visible only to Virtual Private Cloud resources.
     */
    public readonly visibility!: pulumi.Output<string | undefined>;

    /**
     * Create a ManagedZone resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ManagedZoneArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ManagedZoneArgs | ManagedZoneState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ManagedZoneState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["dnsName"] = state ? state.dnsName : undefined;
            inputs["dnssecConfig"] = state ? state.dnssecConfig : undefined;
            inputs["forwardingConfig"] = state ? state.forwardingConfig : undefined;
            inputs["labels"] = state ? state.labels : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["nameServers"] = state ? state.nameServers : undefined;
            inputs["peeringConfig"] = state ? state.peeringConfig : undefined;
            inputs["privateVisibilityConfig"] = state ? state.privateVisibilityConfig : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["reverseLookup"] = state ? state.reverseLookup : undefined;
            inputs["serviceDirectoryConfig"] = state ? state.serviceDirectoryConfig : undefined;
            inputs["visibility"] = state ? state.visibility : undefined;
        } else {
            const args = argsOrState as ManagedZoneArgs | undefined;
            if (!args || args.dnsName === undefined) {
                throw new Error("Missing required property 'dnsName'");
            }
            inputs["description"] = (args ? args.description : undefined) || "Managed by Pulumi";
            inputs["dnsName"] = args ? args.dnsName : undefined;
            inputs["dnssecConfig"] = args ? args.dnssecConfig : undefined;
            inputs["forwardingConfig"] = args ? args.forwardingConfig : undefined;
            inputs["labels"] = args ? args.labels : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["peeringConfig"] = args ? args.peeringConfig : undefined;
            inputs["privateVisibilityConfig"] = args ? args.privateVisibilityConfig : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["reverseLookup"] = args ? args.reverseLookup : undefined;
            inputs["serviceDirectoryConfig"] = args ? args.serviceDirectoryConfig : undefined;
            inputs["visibility"] = args ? args.visibility : undefined;
            inputs["nameServers"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(ManagedZone.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ManagedZone resources.
 */
export interface ManagedZoneState {
    /**
     * A textual description field. Defaults to 'Managed by Pulumi'.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The DNS name of this managed zone, for instance "example.com.".
     */
    readonly dnsName?: pulumi.Input<string>;
    /**
     * DNSSEC configuration  Structure is documented below.
     */
    readonly dnssecConfig?: pulumi.Input<inputs.dns.ManagedZoneDnssecConfig>;
    /**
     * The presence for this field indicates that outbound forwarding is enabled
     * for this zone. The value of this field contains the set of destinations
     * to forward to.  Structure is documented below.
     */
    readonly forwardingConfig?: pulumi.Input<inputs.dns.ManagedZoneForwardingConfig>;
    /**
     * A set of key/value label pairs to assign to this ManagedZone.
     */
    readonly labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * User assigned name for this resource.
     * Must be unique within the project.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Delegate your managed_zone to these virtual name servers; defined by the server
     */
    readonly nameServers?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The presence of this field indicates that DNS Peering is enabled for this
     * zone. The value of this field contains the network to peer with.  Structure is documented below.
     */
    readonly peeringConfig?: pulumi.Input<inputs.dns.ManagedZonePeeringConfig>;
    /**
     * For privately visible zones, the set of Virtual Private Cloud
     * resources that the zone is visible from.  Structure is documented below.
     */
    readonly privateVisibilityConfig?: pulumi.Input<inputs.dns.ManagedZonePrivateVisibilityConfig>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * Specifies if this is a managed reverse lookup zone. If true, Cloud DNS will resolve reverse
     * lookup queries using automatically configured records for VPC resources. This only applies
     * to networks listed under `privateVisibilityConfig`.
     */
    readonly reverseLookup?: pulumi.Input<boolean>;
    /**
     * The presence of this field indicates that this zone is backed by Service Directory. The value of this field contains information related to the namespace associated with the zone.  Structure is documented below.
     */
    readonly serviceDirectoryConfig?: pulumi.Input<inputs.dns.ManagedZoneServiceDirectoryConfig>;
    /**
     * The zone's visibility: public zones are exposed to the Internet,
     * while private zones are visible only to Virtual Private Cloud resources.
     */
    readonly visibility?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ManagedZone resource.
 */
export interface ManagedZoneArgs {
    /**
     * A textual description field. Defaults to 'Managed by Pulumi'.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The DNS name of this managed zone, for instance "example.com.".
     */
    readonly dnsName: pulumi.Input<string>;
    /**
     * DNSSEC configuration  Structure is documented below.
     */
    readonly dnssecConfig?: pulumi.Input<inputs.dns.ManagedZoneDnssecConfig>;
    /**
     * The presence for this field indicates that outbound forwarding is enabled
     * for this zone. The value of this field contains the set of destinations
     * to forward to.  Structure is documented below.
     */
    readonly forwardingConfig?: pulumi.Input<inputs.dns.ManagedZoneForwardingConfig>;
    /**
     * A set of key/value label pairs to assign to this ManagedZone.
     */
    readonly labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * User assigned name for this resource.
     * Must be unique within the project.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The presence of this field indicates that DNS Peering is enabled for this
     * zone. The value of this field contains the network to peer with.  Structure is documented below.
     */
    readonly peeringConfig?: pulumi.Input<inputs.dns.ManagedZonePeeringConfig>;
    /**
     * For privately visible zones, the set of Virtual Private Cloud
     * resources that the zone is visible from.  Structure is documented below.
     */
    readonly privateVisibilityConfig?: pulumi.Input<inputs.dns.ManagedZonePrivateVisibilityConfig>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * Specifies if this is a managed reverse lookup zone. If true, Cloud DNS will resolve reverse
     * lookup queries using automatically configured records for VPC resources. This only applies
     * to networks listed under `privateVisibilityConfig`.
     */
    readonly reverseLookup?: pulumi.Input<boolean>;
    /**
     * The presence of this field indicates that this zone is backed by Service Directory. The value of this field contains information related to the namespace associated with the zone.  Structure is documented below.
     */
    readonly serviceDirectoryConfig?: pulumi.Input<inputs.dns.ManagedZoneServiceDirectoryConfig>;
    /**
     * The zone's visibility: public zones are exposed to the Internet,
     * while private zones are visible only to Virtual Private Cloud resources.
     */
    readonly visibility?: pulumi.Input<string>;
}
