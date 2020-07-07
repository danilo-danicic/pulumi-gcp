// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute.Inputs
{

    public sealed class InstanceBootDiskInitializeParamsGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The image from which to initialize this disk. This can be
        /// one of: the image's `self_link`, `projects/{project}/global/images/{image}`,
        /// `projects/{project}/global/images/family/{family}`, `global/images/{image}`,
        /// `global/images/family/{family}`, `family/{family}`, `{project}/{family}`,
        /// `{project}/{image}`, `{family}`, or `{image}`. If referred by family, the
        /// images names must include the family name. If they don't, use the
        /// [gcp.compute.Image data source](https://www.terraform.io/docs/providers/google/d/compute_image.html).
        /// For instance, the image `centos-6-v20180104` includes its family name `centos-6`.
        /// These images can be referred by family name here.
        /// </summary>
        [Input("image")]
        public Input<string>? Image { get; set; }

        [Input("labels")]
        private InputMap<object>? _labels;

        /// <summary>
        /// A map of key/value label pairs to assign to the instance.
        /// </summary>
        public InputMap<object> Labels
        {
            get => _labels ?? (_labels = new InputMap<object>());
            set => _labels = value;
        }

        /// <summary>
        /// The size of the image in gigabytes. If not specified, it
        /// will inherit the size of its base image.
        /// </summary>
        [Input("size")]
        public Input<int>? Size { get; set; }

        /// <summary>
        /// The accelerator type resource to expose to this instance. E.g. `nvidia-tesla-k80`.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public InstanceBootDiskInitializeParamsGetArgs()
        {
        }
    }
}
