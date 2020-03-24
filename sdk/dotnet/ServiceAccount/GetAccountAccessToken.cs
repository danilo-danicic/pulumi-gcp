// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.ServiceAccount
{
    public static partial class Invokes
    {
        /// <summary>
        /// This data source provides a google `oauth2` `access_token` for a different service account than the one initially running the script.
        /// 
        /// For more information see
        /// [the official documentation](https://cloud.google.com/iam/docs/creating-short-lived-service-account-credentials) as well as [iamcredentials.generateAccessToken()](https://cloud.google.com/iam/credentials/reference/rest/v1/projects.serviceAccounts/generateAccessToken)
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/datasource_google_service_account_access_token.html.markdown.
        /// </summary>
        [Obsolete("Use GetAccountAccessToken.InvokeAsync() instead")]
        public static Task<GetAccountAccessTokenResult> GetAccountAccessToken(GetAccountAccessTokenArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetAccountAccessTokenResult>("gcp:serviceAccount/getAccountAccessToken:getAccountAccessToken", args ?? InvokeArgs.Empty, options.WithVersion());
    }
    public static class GetAccountAccessToken
    {
        /// <summary>
        /// This data source provides a google `oauth2` `access_token` for a different service account than the one initially running the script.
        /// 
        /// For more information see
        /// [the official documentation](https://cloud.google.com/iam/docs/creating-short-lived-service-account-credentials) as well as [iamcredentials.generateAccessToken()](https://cloud.google.com/iam/credentials/reference/rest/v1/projects.serviceAccounts/generateAccessToken)
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/datasource_google_service_account_access_token.html.markdown.
        /// </summary>
        public static Task<GetAccountAccessTokenResult> InvokeAsync(GetAccountAccessTokenArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetAccountAccessTokenResult>("gcp:serviceAccount/getAccountAccessToken:getAccountAccessToken", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetAccountAccessTokenArgs : Pulumi.InvokeArgs
    {
        [Input("delegates")]
        private List<string>? _delegates;

        /// <summary>
        /// Delegate chain of approvals needed to perform full impersonation. Specify the fully qualified service account name.  (e.g. `["projects/-/serviceAccounts/delegate-svc-account@project-id.iam.gserviceaccount.com"]`)
        /// </summary>
        public List<string> Delegates
        {
            get => _delegates ?? (_delegates = new List<string>());
            set => _delegates = value;
        }

        /// <summary>
        /// Lifetime of the impersonated token (defaults to its max: `3600s`).
        /// </summary>
        [Input("lifetime")]
        public string? Lifetime { get; set; }

        [Input("scopes", required: true)]
        private List<string>? _scopes;

        /// <summary>
        /// The scopes the new credential should have (e.g. `["storage-ro", "cloud-platform"]`)
        /// </summary>
        public List<string> Scopes
        {
            get => _scopes ?? (_scopes = new List<string>());
            set => _scopes = value;
        }

        /// <summary>
        /// The service account _to_ impersonate (e.g. `service_B@your-project-id.iam.gserviceaccount.com`)
        /// </summary>
        [Input("targetServiceAccount", required: true)]
        public string TargetServiceAccount { get; set; } = null!;

        public GetAccountAccessTokenArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetAccountAccessTokenResult
    {
        /// <summary>
        /// The `access_token` representing the new generated identity.
        /// </summary>
        public readonly string AccessToken;
        public readonly ImmutableArray<string> Delegates;
        public readonly string? Lifetime;
        public readonly ImmutableArray<string> Scopes;
        public readonly string TargetServiceAccount;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetAccountAccessTokenResult(
            string accessToken,
            ImmutableArray<string> delegates,
            string? lifetime,
            ImmutableArray<string> scopes,
            string targetServiceAccount,
            string id)
        {
            AccessToken = accessToken;
            Delegates = delegates;
            Lifetime = lifetime;
            Scopes = scopes;
            TargetServiceAccount = targetServiceAccount;
            Id = id;
        }
    }
}
