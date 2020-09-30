// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Creates a new Google SQL Database Instance. For more information, see the [official documentation](https://cloud.google.com/sql/),
 * or the [JSON API](https://cloud.google.com/sql/docs/admin-api/v1beta4/instances).
 *
 * > **NOTE on `gcp.sql.DatabaseInstance`:** - First-generation instances have been
 * deprecated and should no longer be created, see [upgrade docs](https://cloud.google.com/sql/docs/mysql/upgrade-2nd-gen)
 * for more details.
 * To upgrade your First-generation instance, update your config that the instance has
 * * `settings.ip_configuration.ipv4_enabled=true`
 * * `settings.backup_configuration.enabled=true`
 * * `settings.backup_configuration.binary_log_enabled=true`.\
 *   Apply the config, then upgrade the instance in the console as described in the documentation.
 *   Once upgraded, update the following attributes in your config to the correct value according to
 *   the above documentation:
 * * `region`
 * * `databaseVersion` (if applicable)
 * * `tier`\
 *   Remove any fields that are not applicable to Second-generation instances:
 * * `settings.crash_safe_replication`
 * * `settings.replication_type`
 * * `settings.authorized_gae_applications`
 *   And change values to appropriate values for Second-generation instances for:
 * * `activationPolicy` ("ON_DEMAND" is no longer an option)
 * * `pricingPlan` ("PER_USE" is now the only valid option)
 *   Change `settings.backup_configuration.enabled` attribute back to its desired value and apply as necessary.
 *
 * > **NOTE on `gcp.sql.DatabaseInstance`:** - Second-generation instances include a
 * default 'root'@'%' user with no password. This user will be deleted by the provider on
 * instance creation. You should use `gcp.sql.User` to define a custom user with
 * a restricted host and strong password.
 *
 * ## Example Usage
 */
export class DatabaseInstance extends pulumi.CustomResource {
    /**
     * Get an existing DatabaseInstance resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatabaseInstanceState, opts?: pulumi.CustomResourceOptions): DatabaseInstance {
        return new DatabaseInstance(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:sql/databaseInstance:DatabaseInstance';

    /**
     * Returns true if the given object is an instance of DatabaseInstance.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DatabaseInstance {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DatabaseInstance.__pulumiType;
    }

    /**
     * The connection name of the instance to be used in
     * connection strings. For example, when connecting with [Cloud SQL Proxy](https://cloud.google.com/sql/docs/mysql/connect-admin-proxy).
     */
    public /*out*/ readonly connectionName!: pulumi.Output<string>;
    /**
     * The MySQL, PostgreSQL or
     * SQL Server (beta) version to use. Supported values include `MYSQL_5_6`,
     * `MYSQL_5_7`, `POSTGRES_9_6`,`POSTGRES_10`, `POSTGRES_11`, `POSTGRES_12`, `SQLSERVER_2017_STANDARD`,
     * `SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`.
     * [Database Version Policies](https://cloud.google.com/sql/docs/sqlserver/db-versions)
     * includes an up-to-date reference of supported versions.
     */
    public readonly databaseVersion!: pulumi.Output<string | undefined>;
    /**
     * The full path to the encryption key used for the CMEK disk encryption.  Setting
     * up disk encryption currently requires manual steps outside of this provider.
     * The provided key must be in the same region as the SQL instance.  In order
     * to use this feature, a special kind of service account must be created and
     * granted permission on this key.  This step can currently only be done
     * manually, please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#service-account).
     * That service account needs the `Cloud KMS > Cloud KMS CryptoKey Encrypter/Decrypter` role on your
     * key - please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#grantkey).
     */
    public readonly encryptionKeyName!: pulumi.Output<string>;
    /**
     * The first IPv4 address of any type assigned.
     */
    public /*out*/ readonly firstIpAddress!: pulumi.Output<string>;
    public /*out*/ readonly ipAddresses!: pulumi.Output<outputs.sql.DatabaseInstanceIpAddress[]>;
    /**
     * The name of the instance that will act as
     * the master in the replication setup. Note, this requires the master to have
     * `binaryLogEnabled` set, as well as existing backups.
     */
    public readonly masterInstanceName!: pulumi.Output<string>;
    /**
     * A name for this whitelist entry.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The first private (`PRIVATE`) IPv4 address assigned.
     */
    public /*out*/ readonly privateIpAddress!: pulumi.Output<string>;
    /**
     * The ID of the project in which the resource belongs. If it
     * is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * The first public (`PRIMARY`) IPv4 address assigned.
     */
    public /*out*/ readonly publicIpAddress!: pulumi.Output<string>;
    /**
     * The region the instance will sit in. Note, Cloud SQL is not
     * available in all regions - choose from one of the options listed [here](https://cloud.google.com/sql/docs/mysql/instance-locations).
     * A valid region must be provided to use this resource. If a region is not provided in the resource definition,
     * the provider region will be used instead, but this will be an apply-time error for instances if the provider
     * region is not supported with Cloud SQL. If you choose not to provide the `region` argument for this resource,
     * make sure you understand this.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * The configuration for replication. The
     * configuration is detailed below.
     */
    public readonly replicaConfiguration!: pulumi.Output<outputs.sql.DatabaseInstanceReplicaConfiguration>;
    /**
     * Initial root password. Required for MS SQL Server, ignored by MySQL and PostgreSQL.
     */
    public readonly rootPassword!: pulumi.Output<string | undefined>;
    /**
     * The URI of the created resource.
     */
    public /*out*/ readonly selfLink!: pulumi.Output<string>;
    public /*out*/ readonly serverCaCerts!: pulumi.Output<outputs.sql.DatabaseInstanceServerCaCert[]>;
    /**
     * The service account email address assigned to the
     * instance.
     */
    public /*out*/ readonly serviceAccountEmailAddress!: pulumi.Output<string>;
    /**
     * The settings to use for the database. The
     * configuration is detailed below.
     */
    public readonly settings!: pulumi.Output<outputs.sql.DatabaseInstanceSettings>;

    /**
     * Create a DatabaseInstance resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DatabaseInstanceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DatabaseInstanceArgs | DatabaseInstanceState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as DatabaseInstanceState | undefined;
            inputs["connectionName"] = state ? state.connectionName : undefined;
            inputs["databaseVersion"] = state ? state.databaseVersion : undefined;
            inputs["encryptionKeyName"] = state ? state.encryptionKeyName : undefined;
            inputs["firstIpAddress"] = state ? state.firstIpAddress : undefined;
            inputs["ipAddresses"] = state ? state.ipAddresses : undefined;
            inputs["masterInstanceName"] = state ? state.masterInstanceName : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["privateIpAddress"] = state ? state.privateIpAddress : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["publicIpAddress"] = state ? state.publicIpAddress : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["replicaConfiguration"] = state ? state.replicaConfiguration : undefined;
            inputs["rootPassword"] = state ? state.rootPassword : undefined;
            inputs["selfLink"] = state ? state.selfLink : undefined;
            inputs["serverCaCerts"] = state ? state.serverCaCerts : undefined;
            inputs["serviceAccountEmailAddress"] = state ? state.serviceAccountEmailAddress : undefined;
            inputs["settings"] = state ? state.settings : undefined;
        } else {
            const args = argsOrState as DatabaseInstanceArgs | undefined;
            if (!args || args.settings === undefined) {
                throw new Error("Missing required property 'settings'");
            }
            inputs["databaseVersion"] = args ? args.databaseVersion : undefined;
            inputs["encryptionKeyName"] = args ? args.encryptionKeyName : undefined;
            inputs["masterInstanceName"] = args ? args.masterInstanceName : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["replicaConfiguration"] = args ? args.replicaConfiguration : undefined;
            inputs["rootPassword"] = args ? args.rootPassword : undefined;
            inputs["settings"] = args ? args.settings : undefined;
            inputs["connectionName"] = undefined /*out*/;
            inputs["firstIpAddress"] = undefined /*out*/;
            inputs["ipAddresses"] = undefined /*out*/;
            inputs["privateIpAddress"] = undefined /*out*/;
            inputs["publicIpAddress"] = undefined /*out*/;
            inputs["selfLink"] = undefined /*out*/;
            inputs["serverCaCerts"] = undefined /*out*/;
            inputs["serviceAccountEmailAddress"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(DatabaseInstance.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DatabaseInstance resources.
 */
export interface DatabaseInstanceState {
    /**
     * The connection name of the instance to be used in
     * connection strings. For example, when connecting with [Cloud SQL Proxy](https://cloud.google.com/sql/docs/mysql/connect-admin-proxy).
     */
    readonly connectionName?: pulumi.Input<string>;
    /**
     * The MySQL, PostgreSQL or
     * SQL Server (beta) version to use. Supported values include `MYSQL_5_6`,
     * `MYSQL_5_7`, `POSTGRES_9_6`,`POSTGRES_10`, `POSTGRES_11`, `POSTGRES_12`, `SQLSERVER_2017_STANDARD`,
     * `SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`.
     * [Database Version Policies](https://cloud.google.com/sql/docs/sqlserver/db-versions)
     * includes an up-to-date reference of supported versions.
     */
    readonly databaseVersion?: pulumi.Input<string>;
    /**
     * The full path to the encryption key used for the CMEK disk encryption.  Setting
     * up disk encryption currently requires manual steps outside of this provider.
     * The provided key must be in the same region as the SQL instance.  In order
     * to use this feature, a special kind of service account must be created and
     * granted permission on this key.  This step can currently only be done
     * manually, please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#service-account).
     * That service account needs the `Cloud KMS > Cloud KMS CryptoKey Encrypter/Decrypter` role on your
     * key - please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#grantkey).
     */
    readonly encryptionKeyName?: pulumi.Input<string>;
    /**
     * The first IPv4 address of any type assigned.
     */
    readonly firstIpAddress?: pulumi.Input<string>;
    readonly ipAddresses?: pulumi.Input<pulumi.Input<inputs.sql.DatabaseInstanceIpAddress>[]>;
    /**
     * The name of the instance that will act as
     * the master in the replication setup. Note, this requires the master to have
     * `binaryLogEnabled` set, as well as existing backups.
     */
    readonly masterInstanceName?: pulumi.Input<string>;
    /**
     * A name for this whitelist entry.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The first private (`PRIVATE`) IPv4 address assigned.
     */
    readonly privateIpAddress?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs. If it
     * is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The first public (`PRIMARY`) IPv4 address assigned.
     */
    readonly publicIpAddress?: pulumi.Input<string>;
    /**
     * The region the instance will sit in. Note, Cloud SQL is not
     * available in all regions - choose from one of the options listed [here](https://cloud.google.com/sql/docs/mysql/instance-locations).
     * A valid region must be provided to use this resource. If a region is not provided in the resource definition,
     * the provider region will be used instead, but this will be an apply-time error for instances if the provider
     * region is not supported with Cloud SQL. If you choose not to provide the `region` argument for this resource,
     * make sure you understand this.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The configuration for replication. The
     * configuration is detailed below.
     */
    readonly replicaConfiguration?: pulumi.Input<inputs.sql.DatabaseInstanceReplicaConfiguration>;
    /**
     * Initial root password. Required for MS SQL Server, ignored by MySQL and PostgreSQL.
     */
    readonly rootPassword?: pulumi.Input<string>;
    /**
     * The URI of the created resource.
     */
    readonly selfLink?: pulumi.Input<string>;
    readonly serverCaCerts?: pulumi.Input<pulumi.Input<inputs.sql.DatabaseInstanceServerCaCert>[]>;
    /**
     * The service account email address assigned to the
     * instance.
     */
    readonly serviceAccountEmailAddress?: pulumi.Input<string>;
    /**
     * The settings to use for the database. The
     * configuration is detailed below.
     */
    readonly settings?: pulumi.Input<inputs.sql.DatabaseInstanceSettings>;
}

/**
 * The set of arguments for constructing a DatabaseInstance resource.
 */
export interface DatabaseInstanceArgs {
    /**
     * The MySQL, PostgreSQL or
     * SQL Server (beta) version to use. Supported values include `MYSQL_5_6`,
     * `MYSQL_5_7`, `POSTGRES_9_6`,`POSTGRES_10`, `POSTGRES_11`, `POSTGRES_12`, `SQLSERVER_2017_STANDARD`,
     * `SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`.
     * [Database Version Policies](https://cloud.google.com/sql/docs/sqlserver/db-versions)
     * includes an up-to-date reference of supported versions.
     */
    readonly databaseVersion?: pulumi.Input<string>;
    /**
     * The full path to the encryption key used for the CMEK disk encryption.  Setting
     * up disk encryption currently requires manual steps outside of this provider.
     * The provided key must be in the same region as the SQL instance.  In order
     * to use this feature, a special kind of service account must be created and
     * granted permission on this key.  This step can currently only be done
     * manually, please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#service-account).
     * That service account needs the `Cloud KMS > Cloud KMS CryptoKey Encrypter/Decrypter` role on your
     * key - please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#grantkey).
     */
    readonly encryptionKeyName?: pulumi.Input<string>;
    /**
     * The name of the instance that will act as
     * the master in the replication setup. Note, this requires the master to have
     * `binaryLogEnabled` set, as well as existing backups.
     */
    readonly masterInstanceName?: pulumi.Input<string>;
    /**
     * A name for this whitelist entry.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs. If it
     * is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The region the instance will sit in. Note, Cloud SQL is not
     * available in all regions - choose from one of the options listed [here](https://cloud.google.com/sql/docs/mysql/instance-locations).
     * A valid region must be provided to use this resource. If a region is not provided in the resource definition,
     * the provider region will be used instead, but this will be an apply-time error for instances if the provider
     * region is not supported with Cloud SQL. If you choose not to provide the `region` argument for this resource,
     * make sure you understand this.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The configuration for replication. The
     * configuration is detailed below.
     */
    readonly replicaConfiguration?: pulumi.Input<inputs.sql.DatabaseInstanceReplicaConfiguration>;
    /**
     * Initial root password. Required for MS SQL Server, ignored by MySQL and PostgreSQL.
     */
    readonly rootPassword?: pulumi.Input<string>;
    /**
     * The settings to use for the database. The
     * configuration is detailed below.
     */
    readonly settings: pulumi.Input<inputs.sql.DatabaseInstanceSettings>;
}
