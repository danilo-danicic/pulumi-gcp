// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * An environment for running orchestration tasks.
 *
 * Environments run Apache Airflow software on Google infrastructure.
 *
 * To get more information about Environments, see:
 *
 * * [API documentation](https://cloud.google.com/composer/docs/reference/rest/)
 * * How-to Guides
 *     * [Official Documentation](https://cloud.google.com/composer/docs)
 *     * [Configuring Shared VPC for Composer Environments](https://cloud.google.com/composer/docs/how-to/managing/configuring-shared-vpc)
 * * [Apache Airflow Documentation](http://airflow.apache.org/)
 *
 * > **Warning:** We **STRONGLY** recommend  you read the [GCP guides](https://cloud.google.com/composer/docs/how-to)
 *   as the Environment resource requires a long deployment process and involves several layers of GCP infrastructure, 
 *   including a Kubernetes Engine cluster, Cloud Storage, and Compute networking resources. Due to limitations of the API,
 *   This provider will not be able to automatically find or manage many of these underlying resources. In particular:
 *   * It can take up to one hour to create or update an environment resource. In addition, GCP may only detect some 
 *     errors in configuration when they are used (e.g. ~40-50 minutes into the creation process), and is prone to limited
 *     error reporting. If you encounter confusing or uninformative errors, please verify your configuration is valid 
 *     against GCP Cloud Composer before filing bugs against this provider. 
 *   * **Environments create Google Cloud Storage buckets that do not get cleaned up automatically** on environment 
 *     deletion. [More about Composer's use of Cloud Storage](https://cloud.google.com/composer/docs/concepts/cloud-storage).
 *
 * ## Example Usage
 *
 * ### Basic Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 *
 * const test = new gcp.composer.Environment("test", {
 *     region: "us-central1",
 * });
 * ```
 *
 * ### With GKE and Compute Resource Dependencies
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 *
 * const testNetwork = new gcp.compute.Network("testNetwork", {autoCreateSubnetworks: false});
 * const testSubnetwork = new gcp.compute.Subnetwork("testSubnetwork", {
 *     ipCidrRange: "10.2.0.0/16",
 *     region: "us-central1",
 *     network: testNetwork.id,
 * });
 * const testAccount = new gcp.serviceAccount.Account("testAccount", {
 *     accountId: "composer-env-account",
 *     displayName: "Test Service Account for Composer Environment",
 * });
 * const composer_worker = new gcp.projects.IAMMember("composer-worker", {
 *     role: "roles/composer.worker",
 *     member: pulumi.interpolate`serviceAccount:${testAccount.email}`,
 * });
 * const testEnvironment = new gcp.composer.Environment("testEnvironment", {
 *     region: "us-central1",
 *     config: {
 *         nodeCount: 4,
 *         node_config: {
 *             zone: "us-central1-a",
 *             machineType: "n1-standard-1",
 *             network: testNetwork.id,
 *             subnetwork: testSubnetwork.id,
 *             serviceAccount: testAccount.name,
 *         },
 *     },
 * });
 * ```
 *
 * ### With Software (Airflow) Config
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 *
 * const test = new gcp.composer.Environment("test", {
 *     config: {
 *         softwareConfig: {
 *             airflowConfigOverrides: {
 *                 "core-load_example": "True",
 *             },
 *             envVariables: {
 *                 FOO: "bar",
 *             },
 *             pypiPackages: {
 *                 numpy: "",
 *                 scipy: "==1.1.0",
 *             },
 *         },
 *     },
 *     region: "us-central1",
 * });
 * ```
 */
export class Environment extends pulumi.CustomResource {
    /**
     * Get an existing Environment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EnvironmentState, opts?: pulumi.CustomResourceOptions): Environment {
        return new Environment(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:composer/environment:Environment';

    /**
     * Returns true if the given object is an instance of Environment.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Environment {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Environment.__pulumiType;
    }

    /**
     * Configuration parameters for this environment  Structure is documented below.
     */
    public readonly config!: pulumi.Output<outputs.composer.EnvironmentConfig>;
    /**
     * User-defined labels for this environment. The labels map can contain
     * no more than 64 entries. Entries of the labels map are UTF8 strings
     * that comply with the following restrictions:
     * Label keys must be between 1 and 63 characters long and must conform
     * to the following regular expression: `a-z?`.
     * Label values must be between 0 and 63 characters long and must
     * conform to the regular expression `(a-z?)?`.
     * No more than 64 labels can be associated with a given environment.
     * Both keys and values must be <= 128 bytes in size.
     */
    public readonly labels!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * Name of the environment
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * The location or Compute Engine region for the environment.
     */
    public readonly region!: pulumi.Output<string | undefined>;

    /**
     * Create a Environment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: EnvironmentArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: EnvironmentArgs | EnvironmentState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as EnvironmentState | undefined;
            inputs["config"] = state ? state.config : undefined;
            inputs["labels"] = state ? state.labels : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["region"] = state ? state.region : undefined;
        } else {
            const args = argsOrState as EnvironmentArgs | undefined;
            inputs["config"] = args ? args.config : undefined;
            inputs["labels"] = args ? args.labels : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["region"] = args ? args.region : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Environment.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Environment resources.
 */
export interface EnvironmentState {
    /**
     * Configuration parameters for this environment  Structure is documented below.
     */
    readonly config?: pulumi.Input<inputs.composer.EnvironmentConfig>;
    /**
     * User-defined labels for this environment. The labels map can contain
     * no more than 64 entries. Entries of the labels map are UTF8 strings
     * that comply with the following restrictions:
     * Label keys must be between 1 and 63 characters long and must conform
     * to the following regular expression: `a-z?`.
     * Label values must be between 0 and 63 characters long and must
     * conform to the regular expression `(a-z?)?`.
     * No more than 64 labels can be associated with a given environment.
     * Both keys and values must be <= 128 bytes in size.
     */
    readonly labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Name of the environment
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The location or Compute Engine region for the environment.
     */
    readonly region?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Environment resource.
 */
export interface EnvironmentArgs {
    /**
     * Configuration parameters for this environment  Structure is documented below.
     */
    readonly config?: pulumi.Input<inputs.composer.EnvironmentConfig>;
    /**
     * User-defined labels for this environment. The labels map can contain
     * no more than 64 entries. Entries of the labels map are UTF8 strings
     * that comply with the following restrictions:
     * Label keys must be between 1 and 63 characters long and must conform
     * to the following regular expression: `a-z?`.
     * Label values must be between 0 and 63 characters long and must
     * conform to the regular expression `(a-z?)?`.
     * No more than 64 labels can be associated with a given environment.
     * Both keys and values must be <= 128 bytes in size.
     */
    readonly labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Name of the environment
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The location or Compute Engine region for the environment.
     */
    readonly region?: pulumi.Input<string>;
}
