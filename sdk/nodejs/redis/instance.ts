// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * A Google Cloud Redis instance.
 *
 *
 * To get more information about Instance, see:
 *
 * * [API documentation](https://cloud.google.com/memorystore/docs/redis/reference/rest/)
 * * How-to Guides
 *     * [Official Documentation](https://cloud.google.com/memorystore/docs/redis/)
 *
 * ## Example Usage
 *
 * ### Redis Instance Basic
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 *
 * const cache = new gcp.redis.Instance("cache", {
 *     memorySizeGb: 1,
 * });
 * ```
 *
 * ### Redis Instance Full
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 *
 * const redis-network = gcp.compute.getNetwork({
 *     name: "redis-test-network",
 * });
 * const cache = new gcp.redis.Instance("cache", {
 *     tier: "STANDARD_HA",
 *     memorySizeGb: 1,
 *     locationId: "us-central1-a",
 *     alternativeLocationId: "us-central1-f",
 *     authorizedNetwork: redis_network.then(redis_network => redis_network.id),
 *     redisVersion: "REDIS_3_2",
 *     displayName: "Test Instance",
 *     reservedIpRange: "192.168.0.0/29",
 *     labels: {
 *         my_key: "my_val",
 *         other_key: "other_val",
 *     },
 * });
 * ```
 */
export class Instance extends pulumi.CustomResource {
    /**
     * Get an existing Instance resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceState, opts?: pulumi.CustomResourceOptions): Instance {
        return new Instance(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:redis/instance:Instance';

    /**
     * Returns true if the given object is an instance of Instance.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Instance {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Instance.__pulumiType;
    }

    /**
     * Only applicable to STANDARD_HA tier which protects the instance
     * against zonal failures by provisioning it across two zones.
     * If provided, it must be a different zone from the one provided in
     * [locationId].
     */
    public readonly alternativeLocationId!: pulumi.Output<string>;
    /**
     * The full name of the Google Compute Engine network to which the
     * instance is connected. If left unspecified, the default network
     * will be used.
     */
    public readonly authorizedNetwork!: pulumi.Output<string>;
    /**
     * The connection mode of the Redis instance.
     */
    public readonly connectMode!: pulumi.Output<string | undefined>;
    /**
     * The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
     */
    public /*out*/ readonly createTime!: pulumi.Output<string>;
    /**
     * The current zone where the Redis endpoint is placed. For Basic Tier instances, this will always be the same as the
     * [locationId] provided by the user at creation time. For Standard Tier instances, this can be either [locationId] or
     * [alternativeLocationId] and can change after a failover event.
     */
    public /*out*/ readonly currentLocationId!: pulumi.Output<string>;
    /**
     * An arbitrary and optional user-provided name for the instance.
     */
    public readonly displayName!: pulumi.Output<string | undefined>;
    /**
     * Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.
     */
    public /*out*/ readonly host!: pulumi.Output<string>;
    /**
     * Resource labels to represent user provided metadata.
     */
    public readonly labels!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * The zone where the instance will be provisioned. If not provided,
     * the service will choose a zone for the instance. For STANDARD_HA tier,
     * instances will be created across two zones for protection against
     * zonal failures. If [alternativeLocationId] is also provided, it must
     * be different from [locationId].
     */
    public readonly locationId!: pulumi.Output<string>;
    /**
     * Redis memory size in GiB.
     */
    public readonly memorySizeGb!: pulumi.Output<number>;
    /**
     * The ID of the instance or a fully qualified identifier for the instance.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The port number of the exposed Redis endpoint.
     */
    public /*out*/ readonly port!: pulumi.Output<number>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * Redis configuration parameters, according to http://redis.io/topics/config.
     * Please check Memorystore documentation for the list of supported parameters:
     * https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
     */
    public readonly redisConfigs!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * The version of Redis software. If not provided, latest supported
     * version will be used. Currently, the supported values are:
     * - REDIS_4_0 for Redis 4.0 compatibility
     * - REDIS_3_2 for Redis 3.2 compatibility
     */
    public readonly redisVersion!: pulumi.Output<string>;
    /**
     * The name of the Redis region of the instance.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * The CIDR range of internal addresses that are reserved for this
     * instance. If not provided, the service will choose an unused /29
     * block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be
     * unique and non-overlapping with existing subnets in an authorized
     * network.
     */
    public readonly reservedIpRange!: pulumi.Output<string>;
    /**
     * The service tier of the instance. Must be one of these values:
     * - BASIC: standalone instance
     * - STANDARD_HA: highly available primary/replica instances
     */
    public readonly tier!: pulumi.Output<string | undefined>;

    /**
     * Create a Instance resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: InstanceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: InstanceArgs | InstanceState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as InstanceState | undefined;
            inputs["alternativeLocationId"] = state ? state.alternativeLocationId : undefined;
            inputs["authorizedNetwork"] = state ? state.authorizedNetwork : undefined;
            inputs["connectMode"] = state ? state.connectMode : undefined;
            inputs["createTime"] = state ? state.createTime : undefined;
            inputs["currentLocationId"] = state ? state.currentLocationId : undefined;
            inputs["displayName"] = state ? state.displayName : undefined;
            inputs["host"] = state ? state.host : undefined;
            inputs["labels"] = state ? state.labels : undefined;
            inputs["locationId"] = state ? state.locationId : undefined;
            inputs["memorySizeGb"] = state ? state.memorySizeGb : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["port"] = state ? state.port : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["redisConfigs"] = state ? state.redisConfigs : undefined;
            inputs["redisVersion"] = state ? state.redisVersion : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["reservedIpRange"] = state ? state.reservedIpRange : undefined;
            inputs["tier"] = state ? state.tier : undefined;
        } else {
            const args = argsOrState as InstanceArgs | undefined;
            if (!args || args.memorySizeGb === undefined) {
                throw new Error("Missing required property 'memorySizeGb'");
            }
            inputs["alternativeLocationId"] = args ? args.alternativeLocationId : undefined;
            inputs["authorizedNetwork"] = args ? args.authorizedNetwork : undefined;
            inputs["connectMode"] = args ? args.connectMode : undefined;
            inputs["displayName"] = args ? args.displayName : undefined;
            inputs["labels"] = args ? args.labels : undefined;
            inputs["locationId"] = args ? args.locationId : undefined;
            inputs["memorySizeGb"] = args ? args.memorySizeGb : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["redisConfigs"] = args ? args.redisConfigs : undefined;
            inputs["redisVersion"] = args ? args.redisVersion : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["reservedIpRange"] = args ? args.reservedIpRange : undefined;
            inputs["tier"] = args ? args.tier : undefined;
            inputs["createTime"] = undefined /*out*/;
            inputs["currentLocationId"] = undefined /*out*/;
            inputs["host"] = undefined /*out*/;
            inputs["port"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Instance.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Instance resources.
 */
export interface InstanceState {
    /**
     * Only applicable to STANDARD_HA tier which protects the instance
     * against zonal failures by provisioning it across two zones.
     * If provided, it must be a different zone from the one provided in
     * [locationId].
     */
    readonly alternativeLocationId?: pulumi.Input<string>;
    /**
     * The full name of the Google Compute Engine network to which the
     * instance is connected. If left unspecified, the default network
     * will be used.
     */
    readonly authorizedNetwork?: pulumi.Input<string>;
    /**
     * The connection mode of the Redis instance.
     */
    readonly connectMode?: pulumi.Input<string>;
    /**
     * The time the instance was created in RFC3339 UTC "Zulu" format, accurate to nanoseconds.
     */
    readonly createTime?: pulumi.Input<string>;
    /**
     * The current zone where the Redis endpoint is placed. For Basic Tier instances, this will always be the same as the
     * [locationId] provided by the user at creation time. For Standard Tier instances, this can be either [locationId] or
     * [alternativeLocationId] and can change after a failover event.
     */
    readonly currentLocationId?: pulumi.Input<string>;
    /**
     * An arbitrary and optional user-provided name for the instance.
     */
    readonly displayName?: pulumi.Input<string>;
    /**
     * Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.
     */
    readonly host?: pulumi.Input<string>;
    /**
     * Resource labels to represent user provided metadata.
     */
    readonly labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The zone where the instance will be provisioned. If not provided,
     * the service will choose a zone for the instance. For STANDARD_HA tier,
     * instances will be created across two zones for protection against
     * zonal failures. If [alternativeLocationId] is also provided, it must
     * be different from [locationId].
     */
    readonly locationId?: pulumi.Input<string>;
    /**
     * Redis memory size in GiB.
     */
    readonly memorySizeGb?: pulumi.Input<number>;
    /**
     * The ID of the instance or a fully qualified identifier for the instance.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The port number of the exposed Redis endpoint.
     */
    readonly port?: pulumi.Input<number>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * Redis configuration parameters, according to http://redis.io/topics/config.
     * Please check Memorystore documentation for the list of supported parameters:
     * https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
     */
    readonly redisConfigs?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The version of Redis software. If not provided, latest supported
     * version will be used. Currently, the supported values are:
     * - REDIS_4_0 for Redis 4.0 compatibility
     * - REDIS_3_2 for Redis 3.2 compatibility
     */
    readonly redisVersion?: pulumi.Input<string>;
    /**
     * The name of the Redis region of the instance.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The CIDR range of internal addresses that are reserved for this
     * instance. If not provided, the service will choose an unused /29
     * block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be
     * unique and non-overlapping with existing subnets in an authorized
     * network.
     */
    readonly reservedIpRange?: pulumi.Input<string>;
    /**
     * The service tier of the instance. Must be one of these values:
     * - BASIC: standalone instance
     * - STANDARD_HA: highly available primary/replica instances
     */
    readonly tier?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Instance resource.
 */
export interface InstanceArgs {
    /**
     * Only applicable to STANDARD_HA tier which protects the instance
     * against zonal failures by provisioning it across two zones.
     * If provided, it must be a different zone from the one provided in
     * [locationId].
     */
    readonly alternativeLocationId?: pulumi.Input<string>;
    /**
     * The full name of the Google Compute Engine network to which the
     * instance is connected. If left unspecified, the default network
     * will be used.
     */
    readonly authorizedNetwork?: pulumi.Input<string>;
    /**
     * The connection mode of the Redis instance.
     */
    readonly connectMode?: pulumi.Input<string>;
    /**
     * An arbitrary and optional user-provided name for the instance.
     */
    readonly displayName?: pulumi.Input<string>;
    /**
     * Resource labels to represent user provided metadata.
     */
    readonly labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The zone where the instance will be provisioned. If not provided,
     * the service will choose a zone for the instance. For STANDARD_HA tier,
     * instances will be created across two zones for protection against
     * zonal failures. If [alternativeLocationId] is also provided, it must
     * be different from [locationId].
     */
    readonly locationId?: pulumi.Input<string>;
    /**
     * Redis memory size in GiB.
     */
    readonly memorySizeGb: pulumi.Input<number>;
    /**
     * The ID of the instance or a fully qualified identifier for the instance.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * Redis configuration parameters, according to http://redis.io/topics/config.
     * Please check Memorystore documentation for the list of supported parameters:
     * https://cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_configs
     */
    readonly redisConfigs?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The version of Redis software. If not provided, latest supported
     * version will be used. Currently, the supported values are:
     * - REDIS_4_0 for Redis 4.0 compatibility
     * - REDIS_3_2 for Redis 3.2 compatibility
     */
    readonly redisVersion?: pulumi.Input<string>;
    /**
     * The name of the Redis region of the instance.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The CIDR range of internal addresses that are reserved for this
     * instance. If not provided, the service will choose an unused /29
     * block, for example, 10.0.0.0/29 or 192.168.0.0/29. Ranges must be
     * unique and non-overlapping with existing subnets in an authorized
     * network.
     */
    readonly reservedIpRange?: pulumi.Input<string>;
    /**
     * The service tier of the instance. Must be one of these values:
     * - BASIC: standalone instance
     * - STANDARD_HA: highly available primary/replica instances
     */
    readonly tier?: pulumi.Input<string>;
}
