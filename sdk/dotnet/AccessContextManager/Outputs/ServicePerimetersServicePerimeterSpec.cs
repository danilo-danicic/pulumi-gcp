// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.AccessContextManager.Outputs
{

    [OutputType]
    public sealed class ServicePerimetersServicePerimeterSpec
    {
        /// <summary>
        /// A list of AccessLevel resource names that allow resources within
        /// the ServicePerimeter to be accessed from the internet.
        /// AccessLevels listed must be in the same policy as this
        /// ServicePerimeter. Referencing a nonexistent AccessLevel is a
        /// syntax error. If no AccessLevel names are listed, resources within
        /// the perimeter can only be accessed via GCP calls with request
        /// origins within the perimeter. For Service Perimeter Bridge, must
        /// be empty.
        /// Format: accessPolicies/{policy_id}/accessLevels/{access_level_name}
        /// </summary>
        public readonly ImmutableArray<string> AccessLevels;
        /// <summary>
        /// A list of GCP resources that are inside of the service perimeter.
        /// Currently only projects are allowed.
        /// Format: projects/{project_number}
        /// </summary>
        public readonly ImmutableArray<string> Resources;
        /// <summary>
        /// GCP services that are subject to the Service Perimeter
        /// restrictions. Must contain a list of services. For example, if
        /// `storage.googleapis.com` is specified, access to the storage
        /// buckets inside the perimeter must meet the perimeter's access
        /// restrictions.
        /// </summary>
        public readonly ImmutableArray<string> RestrictedServices;
        /// <summary>
        /// Specifies how APIs are allowed to communicate within the Service
        /// Perimeter.
        /// Structure is documented below.
        /// </summary>
        public readonly Outputs.ServicePerimetersServicePerimeterSpecVpcAccessibleServices? VpcAccessibleServices;

        [OutputConstructor]
        private ServicePerimetersServicePerimeterSpec(
            ImmutableArray<string> accessLevels,

            ImmutableArray<string> resources,

            ImmutableArray<string> restrictedServices,

            Outputs.ServicePerimetersServicePerimeterSpecVpcAccessibleServices? vpcAccessibleServices)
        {
            AccessLevels = accessLevels;
            Resources = resources;
            RestrictedServices = restrictedServices;
            VpcAccessibleServices = vpcAccessibleServices;
        }
    }
}
