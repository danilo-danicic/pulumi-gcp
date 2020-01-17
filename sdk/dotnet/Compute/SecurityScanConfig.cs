// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute
{
    /// <summary>
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/security_scanner_scan_config.html.markdown.
    /// </summary>
    public partial class SecurityScanConfig : Pulumi.CustomResource
    {
        /// <summary>
        /// The authentication configuration. If specified, service will use the authentication configuration during
        /// scanning.
        /// </summary>
        [Output("authentication")]
        public Output<Outputs.SecurityScanConfigAuthentication?> Authentication { get; private set; } = null!;

        /// <summary>
        /// The blacklist URL patterns as described in https://cloud.google.com/security-scanner/docs/excluded-urls
        /// </summary>
        [Output("blacklistPatterns")]
        public Output<ImmutableArray<string>> BlacklistPatterns { get; private set; } = null!;

        /// <summary>
        /// The user provider display name of the ScanConfig.
        /// </summary>
        [Output("displayName")]
        public Output<string> DisplayName { get; private set; } = null!;

        /// <summary>
        /// Controls export of scan configurations and results to Cloud Security Command Center.
        /// </summary>
        [Output("exportToSecurityCommandCenter")]
        public Output<string?> ExportToSecurityCommandCenter { get; private set; } = null!;

        /// <summary>
        /// The maximum QPS during scanning. A valid value ranges from 5 to 20 inclusively. Defaults to 15.
        /// </summary>
        [Output("maxQps")]
        public Output<int?> MaxQps { get; private set; } = null!;

        /// <summary>
        /// A server defined name for this index. Format: 'projects/{{project}}/scanConfigs/{{server_generated_id}}'
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// The schedule of the ScanConfig
        /// </summary>
        [Output("schedule")]
        public Output<Outputs.SecurityScanConfigSchedule?> Schedule { get; private set; } = null!;

        /// <summary>
        /// The starting URLs from which the scanner finds site pages.
        /// </summary>
        [Output("startingUrls")]
        public Output<ImmutableArray<string>> StartingUrls { get; private set; } = null!;

        /// <summary>
        /// Set of Cloud Platforms targeted by the scan. If empty, APP_ENGINE will be used as a default.
        /// </summary>
        [Output("targetPlatforms")]
        public Output<ImmutableArray<string>> TargetPlatforms { get; private set; } = null!;

        /// <summary>
        /// Type of the user agents used for scanning
        /// </summary>
        [Output("userAgent")]
        public Output<string?> UserAgent { get; private set; } = null!;


        /// <summary>
        /// Create a SecurityScanConfig resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SecurityScanConfig(string name, SecurityScanConfigArgs args, CustomResourceOptions? options = null)
            : base("gcp:compute/securityScanConfig:SecurityScanConfig", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private SecurityScanConfig(string name, Input<string> id, SecurityScanConfigState? state = null, CustomResourceOptions? options = null)
            : base("gcp:compute/securityScanConfig:SecurityScanConfig", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing SecurityScanConfig resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SecurityScanConfig Get(string name, Input<string> id, SecurityScanConfigState? state = null, CustomResourceOptions? options = null)
        {
            return new SecurityScanConfig(name, id, state, options);
        }
    }

    public sealed class SecurityScanConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The authentication configuration. If specified, service will use the authentication configuration during
        /// scanning.
        /// </summary>
        [Input("authentication")]
        public Input<Inputs.SecurityScanConfigAuthenticationArgs>? Authentication { get; set; }

        [Input("blacklistPatterns")]
        private InputList<string>? _blacklistPatterns;

        /// <summary>
        /// The blacklist URL patterns as described in https://cloud.google.com/security-scanner/docs/excluded-urls
        /// </summary>
        public InputList<string> BlacklistPatterns
        {
            get => _blacklistPatterns ?? (_blacklistPatterns = new InputList<string>());
            set => _blacklistPatterns = value;
        }

        /// <summary>
        /// The user provider display name of the ScanConfig.
        /// </summary>
        [Input("displayName", required: true)]
        public Input<string> DisplayName { get; set; } = null!;

        /// <summary>
        /// Controls export of scan configurations and results to Cloud Security Command Center.
        /// </summary>
        [Input("exportToSecurityCommandCenter")]
        public Input<string>? ExportToSecurityCommandCenter { get; set; }

        /// <summary>
        /// The maximum QPS during scanning. A valid value ranges from 5 to 20 inclusively. Defaults to 15.
        /// </summary>
        [Input("maxQps")]
        public Input<int>? MaxQps { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// The schedule of the ScanConfig
        /// </summary>
        [Input("schedule")]
        public Input<Inputs.SecurityScanConfigScheduleArgs>? Schedule { get; set; }

        [Input("startingUrls", required: true)]
        private InputList<string>? _startingUrls;

        /// <summary>
        /// The starting URLs from which the scanner finds site pages.
        /// </summary>
        public InputList<string> StartingUrls
        {
            get => _startingUrls ?? (_startingUrls = new InputList<string>());
            set => _startingUrls = value;
        }

        [Input("targetPlatforms")]
        private InputList<string>? _targetPlatforms;

        /// <summary>
        /// Set of Cloud Platforms targeted by the scan. If empty, APP_ENGINE will be used as a default.
        /// </summary>
        public InputList<string> TargetPlatforms
        {
            get => _targetPlatforms ?? (_targetPlatforms = new InputList<string>());
            set => _targetPlatforms = value;
        }

        /// <summary>
        /// Type of the user agents used for scanning
        /// </summary>
        [Input("userAgent")]
        public Input<string>? UserAgent { get; set; }

        public SecurityScanConfigArgs()
        {
        }
    }

    public sealed class SecurityScanConfigState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The authentication configuration. If specified, service will use the authentication configuration during
        /// scanning.
        /// </summary>
        [Input("authentication")]
        public Input<Inputs.SecurityScanConfigAuthenticationGetArgs>? Authentication { get; set; }

        [Input("blacklistPatterns")]
        private InputList<string>? _blacklistPatterns;

        /// <summary>
        /// The blacklist URL patterns as described in https://cloud.google.com/security-scanner/docs/excluded-urls
        /// </summary>
        public InputList<string> BlacklistPatterns
        {
            get => _blacklistPatterns ?? (_blacklistPatterns = new InputList<string>());
            set => _blacklistPatterns = value;
        }

        /// <summary>
        /// The user provider display name of the ScanConfig.
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// Controls export of scan configurations and results to Cloud Security Command Center.
        /// </summary>
        [Input("exportToSecurityCommandCenter")]
        public Input<string>? ExportToSecurityCommandCenter { get; set; }

        /// <summary>
        /// The maximum QPS during scanning. A valid value ranges from 5 to 20 inclusively. Defaults to 15.
        /// </summary>
        [Input("maxQps")]
        public Input<int>? MaxQps { get; set; }

        /// <summary>
        /// A server defined name for this index. Format: 'projects/{{project}}/scanConfigs/{{server_generated_id}}'
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// The schedule of the ScanConfig
        /// </summary>
        [Input("schedule")]
        public Input<Inputs.SecurityScanConfigScheduleGetArgs>? Schedule { get; set; }

        [Input("startingUrls")]
        private InputList<string>? _startingUrls;

        /// <summary>
        /// The starting URLs from which the scanner finds site pages.
        /// </summary>
        public InputList<string> StartingUrls
        {
            get => _startingUrls ?? (_startingUrls = new InputList<string>());
            set => _startingUrls = value;
        }

        [Input("targetPlatforms")]
        private InputList<string>? _targetPlatforms;

        /// <summary>
        /// Set of Cloud Platforms targeted by the scan. If empty, APP_ENGINE will be used as a default.
        /// </summary>
        public InputList<string> TargetPlatforms
        {
            get => _targetPlatforms ?? (_targetPlatforms = new InputList<string>());
            set => _targetPlatforms = value;
        }

        /// <summary>
        /// Type of the user agents used for scanning
        /// </summary>
        [Input("userAgent")]
        public Input<string>? UserAgent { get; set; }

        public SecurityScanConfigState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class SecurityScanConfigAuthenticationArgs : Pulumi.ResourceArgs
    {
        [Input("customAccount")]
        public Input<SecurityScanConfigAuthenticationCustomAccountArgs>? CustomAccount { get; set; }

        [Input("googleAccount")]
        public Input<SecurityScanConfigAuthenticationGoogleAccountArgs>? GoogleAccount { get; set; }

        public SecurityScanConfigAuthenticationArgs()
        {
        }
    }

    public sealed class SecurityScanConfigAuthenticationCustomAccountArgs : Pulumi.ResourceArgs
    {
        [Input("loginUrl", required: true)]
        public Input<string> LoginUrl { get; set; } = null!;

        [Input("password", required: true)]
        public Input<string> Password { get; set; } = null!;

        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        public SecurityScanConfigAuthenticationCustomAccountArgs()
        {
        }
    }

    public sealed class SecurityScanConfigAuthenticationCustomAccountGetArgs : Pulumi.ResourceArgs
    {
        [Input("loginUrl", required: true)]
        public Input<string> LoginUrl { get; set; } = null!;

        [Input("password", required: true)]
        public Input<string> Password { get; set; } = null!;

        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        public SecurityScanConfigAuthenticationCustomAccountGetArgs()
        {
        }
    }

    public sealed class SecurityScanConfigAuthenticationGetArgs : Pulumi.ResourceArgs
    {
        [Input("customAccount")]
        public Input<SecurityScanConfigAuthenticationCustomAccountGetArgs>? CustomAccount { get; set; }

        [Input("googleAccount")]
        public Input<SecurityScanConfigAuthenticationGoogleAccountGetArgs>? GoogleAccount { get; set; }

        public SecurityScanConfigAuthenticationGetArgs()
        {
        }
    }

    public sealed class SecurityScanConfigAuthenticationGoogleAccountArgs : Pulumi.ResourceArgs
    {
        [Input("password", required: true)]
        public Input<string> Password { get; set; } = null!;

        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        public SecurityScanConfigAuthenticationGoogleAccountArgs()
        {
        }
    }

    public sealed class SecurityScanConfigAuthenticationGoogleAccountGetArgs : Pulumi.ResourceArgs
    {
        [Input("password", required: true)]
        public Input<string> Password { get; set; } = null!;

        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        public SecurityScanConfigAuthenticationGoogleAccountGetArgs()
        {
        }
    }

    public sealed class SecurityScanConfigScheduleArgs : Pulumi.ResourceArgs
    {
        [Input("intervalDurationDays", required: true)]
        public Input<int> IntervalDurationDays { get; set; } = null!;

        [Input("scheduleTime")]
        public Input<string>? ScheduleTime { get; set; }

        public SecurityScanConfigScheduleArgs()
        {
        }
    }

    public sealed class SecurityScanConfigScheduleGetArgs : Pulumi.ResourceArgs
    {
        [Input("intervalDurationDays", required: true)]
        public Input<int> IntervalDurationDays { get; set; } = null!;

        [Input("scheduleTime")]
        public Input<string>? ScheduleTime { get; set; }

        public SecurityScanConfigScheduleGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class SecurityScanConfigAuthentication
    {
        public readonly SecurityScanConfigAuthenticationCustomAccount? CustomAccount;
        public readonly SecurityScanConfigAuthenticationGoogleAccount? GoogleAccount;

        [OutputConstructor]
        private SecurityScanConfigAuthentication(
            SecurityScanConfigAuthenticationCustomAccount? customAccount,
            SecurityScanConfigAuthenticationGoogleAccount? googleAccount)
        {
            CustomAccount = customAccount;
            GoogleAccount = googleAccount;
        }
    }

    [OutputType]
    public sealed class SecurityScanConfigAuthenticationCustomAccount
    {
        public readonly string LoginUrl;
        public readonly string Password;
        public readonly string Username;

        [OutputConstructor]
        private SecurityScanConfigAuthenticationCustomAccount(
            string loginUrl,
            string password,
            string username)
        {
            LoginUrl = loginUrl;
            Password = password;
            Username = username;
        }
    }

    [OutputType]
    public sealed class SecurityScanConfigAuthenticationGoogleAccount
    {
        public readonly string Password;
        public readonly string Username;

        [OutputConstructor]
        private SecurityScanConfigAuthenticationGoogleAccount(
            string password,
            string username)
        {
            Password = password;
            Username = username;
        }
    }

    [OutputType]
    public sealed class SecurityScanConfigSchedule
    {
        public readonly int IntervalDurationDays;
        public readonly string? ScheduleTime;

        [OutputConstructor]
        private SecurityScanConfigSchedule(
            int intervalDurationDays,
            string? scheduleTime)
        {
            IntervalDurationDays = intervalDurationDays;
            ScheduleTime = scheduleTime;
        }
    }
    }
}