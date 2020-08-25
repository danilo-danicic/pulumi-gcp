// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.AccessContextManager.Inputs
{

    public sealed class ServicePerimetersServicePerimeterStatusArgs : Pulumi.ResourceArgs
    {
        [Input("accessLevels")]
        private InputList<string>? _accessLevels;

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
        public InputList<string> AccessLevels
        {
            get => _accessLevels ?? (_accessLevels = new InputList<string>());
            set => _accessLevels = value;
        }

        [Input("resources")]
        private InputList<string>? _resources;

        /// <summary>
        /// A list of GCP resources that are inside of the service perimeter.
        /// Currently only projects are allowed.
        /// Format: projects/{project_number}
        /// </summary>
        public InputList<string> Resources
        {
            get => _resources ?? (_resources = new InputList<string>());
            set => _resources = value;
        }

        [Input("restrictedServices")]
        private InputList<string>? _restrictedServices;

        /// <summary>
        /// GCP services that are subject to the Service Perimeter
        /// restrictions. Must contain a list of services. For example, if
        /// `storage.googleapis.com` is specified, access to the storage
        /// buckets inside the perimeter must meet the perimeter's access
        /// restrictions.
        /// </summary>
        public InputList<string> RestrictedServices
        {
            get => _restrictedServices ?? (_restrictedServices = new InputList<string>());
            set => _restrictedServices = value;
        }

        /// <summary>
        /// Specifies how APIs are allowed to communicate within the Service
        /// Perimeter.
        /// Structure is documented below.
        /// </summary>
        [Input("vpcAccessibleServices")]
        public Input<Inputs.ServicePerimetersServicePerimeterStatusVpcAccessibleServicesArgs>? VpcAccessibleServices { get; set; }

        public ServicePerimetersServicePerimeterStatusArgs()
        {
        }
    }
}
