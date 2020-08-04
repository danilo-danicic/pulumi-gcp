// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute.Outputs
{

    [OutputType]
    public sealed class RegionUrlMapDefaultUrlRedirect
    {
        /// <summary>
        /// The host that will be used in the redirect response instead of the one that was
        /// supplied in the request. The value must be between 1 and 255 characters.
        /// </summary>
        public readonly string? HostRedirect;
        /// <summary>
        /// If set to true, the URL scheme in the redirected request is set to https. If set to
        /// false, the URL scheme of the redirected request will remain the same as that of the
        /// request. This must only be set for UrlMaps used in TargetHttpProxys. Setting this
        /// true for TargetHttpsProxy is not permitted. The default is set to false.
        /// </summary>
        public readonly bool? HttpsRedirect;
        /// <summary>
        /// The path that will be used in the redirect response instead of the one that was
        /// supplied in the request. pathRedirect cannot be supplied together with
        /// prefixRedirect. Supply one alone or neither. If neither is supplied, the path of the
        /// original request will be used for the redirect. The value must be between 1 and 1024
        /// characters.
        /// </summary>
        public readonly string? PathRedirect;
        /// <summary>
        /// The prefix that replaces the prefixMatch specified in the HttpRouteRuleMatch,
        /// retaining the remaining portion of the URL before redirecting the request.
        /// prefixRedirect cannot be supplied together with pathRedirect. Supply one alone or
        /// neither. If neither is supplied, the path of the original request will be used for
        /// the redirect. The value must be between 1 and 1024 characters.
        /// </summary>
        public readonly string? PrefixRedirect;
        /// <summary>
        /// The HTTP Status code to use for this RedirectAction. Supported values are:
        /// * MOVED_PERMANENTLY_DEFAULT, which is the default value and corresponds to 301.
        /// * FOUND, which corresponds to 302.
        /// * SEE_OTHER which corresponds to 303.
        /// * TEMPORARY_REDIRECT, which corresponds to 307. In this case, the request method
        /// will be retained.
        /// * PERMANENT_REDIRECT, which corresponds to 308. In this case,
        /// the request method will be retained.
        /// </summary>
        public readonly string? RedirectResponseCode;
        /// <summary>
        /// If set to true, any accompanying query portion of the original URL is removed prior
        /// to redirecting the request. If set to false, the query portion of the original URL is
        /// retained.
        /// This field is required to ensure an empty block is not set. The normal default value is false.
        /// </summary>
        public readonly bool StripQuery;

        [OutputConstructor]
        private RegionUrlMapDefaultUrlRedirect(
            string? hostRedirect,

            bool? httpsRedirect,

            string? pathRedirect,

            string? prefixRedirect,

            string? redirectResponseCode,

            bool stripQuery)
        {
            HostRedirect = hostRedirect;
            HttpsRedirect = httpsRedirect;
            PathRedirect = pathRedirect;
            PrefixRedirect = prefixRedirect;
            RedirectResponseCode = redirectResponseCode;
            StripQuery = stripQuery;
        }
    }
}
