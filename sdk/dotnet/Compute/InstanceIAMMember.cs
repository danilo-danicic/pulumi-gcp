// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute
{
    /// <summary>
    /// Three different resources help you manage your IAM policy for Compute Engine Instance. Each of these resources serves a different use case:
    /// 
    /// * `gcp.compute.InstanceIAMPolicy`: Authoritative. Sets the IAM policy for the instance and replaces any existing policy already attached.
    /// * `gcp.compute.InstanceIAMBinding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the instance are preserved.
    /// * `gcp.compute.InstanceIAMMember`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the instance are preserved.
    /// 
    /// &gt; **Note:** `gcp.compute.InstanceIAMPolicy` **cannot** be used in conjunction with `gcp.compute.InstanceIAMBinding` and `gcp.compute.InstanceIAMMember` or they will fight over what your policy should be.
    /// 
    /// &gt; **Note:** `gcp.compute.InstanceIAMBinding` resources **can be** used in conjunction with `gcp.compute.InstanceIAMMember` resources **only if** they do not grant privilege to the same role.
    /// 
    /// ## google\_compute\_instance\_iam\_policy
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Gcp = Pulumi.Gcp;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var admin = Output.Create(Gcp.Organizations.GetIAMPolicy.InvokeAsync(new Gcp.Organizations.GetIAMPolicyArgs
    ///         {
    ///             Binding = 
    ///             {
    ///                 
    ///                 {
    ///                     { "role", "roles/compute.osLogin" },
    ///                     { "members", 
    ///                     {
    ///                         "user:jane@example.com",
    ///                     } },
    ///                 },
    ///             },
    ///         }));
    ///         var policy = new Gcp.Compute.InstanceIAMPolicy("policy", new Gcp.Compute.InstanceIAMPolicyArgs
    ///         {
    ///             Project = google_compute_instance.Default.Project,
    ///             Zone = google_compute_instance.Default.Zone,
    ///             InstanceName = google_compute_instance.Default.Name,
    ///             PolicyData = admin.Apply(admin =&gt; admin.PolicyData),
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// With IAM Conditions:
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Gcp = Pulumi.Gcp;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var admin = Output.Create(Gcp.Organizations.GetIAMPolicy.InvokeAsync(new Gcp.Organizations.GetIAMPolicyArgs
    ///         {
    ///             Binding = 
    ///             {
    ///                 
    ///                 {
    ///                     { "role", "roles/compute.osLogin" },
    ///                     { "members", 
    ///                     {
    ///                         "user:jane@example.com",
    ///                     } },
    ///                     { "condition", 
    ///                     {
    ///                         { "title", "expires_after_2019_12_31" },
    ///                         { "description", "Expiring at midnight of 2019-12-31" },
    ///                         { "expression", "request.time &lt; timestamp(\"2020-01-01T00:00:00Z\")" },
    ///                     } },
    ///                 },
    ///             },
    ///         }));
    ///         var policy = new Gcp.Compute.InstanceIAMPolicy("policy", new Gcp.Compute.InstanceIAMPolicyArgs
    ///         {
    ///             Project = google_compute_instance.Default.Project,
    ///             Zone = google_compute_instance.Default.Zone,
    ///             InstanceName = google_compute_instance.Default.Name,
    ///             PolicyData = admin.Apply(admin =&gt; admin.PolicyData),
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ## google\_compute\_instance\_iam\_binding
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Gcp = Pulumi.Gcp;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var binding = new Gcp.Compute.InstanceIAMBinding("binding", new Gcp.Compute.InstanceIAMBindingArgs
    ///         {
    ///             Project = google_compute_instance.Default.Project,
    ///             Zone = google_compute_instance.Default.Zone,
    ///             InstanceName = google_compute_instance.Default.Name,
    ///             Role = "roles/compute.osLogin",
    ///             Members = 
    ///             {
    ///                 "user:jane@example.com",
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// With IAM Conditions:
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Gcp = Pulumi.Gcp;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var binding = new Gcp.Compute.InstanceIAMBinding("binding", new Gcp.Compute.InstanceIAMBindingArgs
    ///         {
    ///             Project = google_compute_instance.Default.Project,
    ///             Zone = google_compute_instance.Default.Zone,
    ///             InstanceName = google_compute_instance.Default.Name,
    ///             Role = "roles/compute.osLogin",
    ///             Members = 
    ///             {
    ///                 "user:jane@example.com",
    ///             },
    ///             Condition = new Gcp.Compute.Inputs.InstanceIAMBindingConditionArgs
    ///             {
    ///                 Title = "expires_after_2019_12_31",
    ///                 Description = "Expiring at midnight of 2019-12-31",
    ///                 Expression = "request.time &lt; timestamp(\"2020-01-01T00:00:00Z\")",
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ## google\_compute\_instance\_iam\_member
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Gcp = Pulumi.Gcp;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var member = new Gcp.Compute.InstanceIAMMember("member", new Gcp.Compute.InstanceIAMMemberArgs
    ///         {
    ///             Project = google_compute_instance.Default.Project,
    ///             Zone = google_compute_instance.Default.Zone,
    ///             InstanceName = google_compute_instance.Default.Name,
    ///             Role = "roles/compute.osLogin",
    ///             Member = "user:jane@example.com",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// With IAM Conditions:
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Gcp = Pulumi.Gcp;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var member = new Gcp.Compute.InstanceIAMMember("member", new Gcp.Compute.InstanceIAMMemberArgs
    ///         {
    ///             Project = google_compute_instance.Default.Project,
    ///             Zone = google_compute_instance.Default.Zone,
    ///             InstanceName = google_compute_instance.Default.Name,
    ///             Role = "roles/compute.osLogin",
    ///             Member = "user:jane@example.com",
    ///             Condition = new Gcp.Compute.Inputs.InstanceIAMMemberConditionArgs
    ///             {
    ///                 Title = "expires_after_2019_12_31",
    ///                 Description = "Expiring at midnight of 2019-12-31",
    ///                 Expression = "request.time &lt; timestamp(\"2020-01-01T00:00:00Z\")",
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class InstanceIAMMember : Pulumi.CustomResource
    {
        /// <summary>
        /// ) An [IAM Condition](https://cloud.google.com/iam/docs/conditions-overview) for a given binding.
        /// Structure is documented below.
        /// </summary>
        [Output("condition")]
        public Output<Outputs.InstanceIAMMemberCondition?> Condition { get; private set; } = null!;

        /// <summary>
        /// (Computed) The etag of the IAM policy.
        /// </summary>
        [Output("etag")]
        public Output<string> Etag { get; private set; } = null!;

        /// <summary>
        /// Used to find the parent resource to bind the IAM policy to
        /// </summary>
        [Output("instanceName")]
        public Output<string> InstanceName { get; private set; } = null!;

        [Output("member")]
        public Output<string> Member { get; private set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
        /// </summary>
        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// The role that should be applied. Only one
        /// `gcp.compute.InstanceIAMBinding` can be used per role. Note that custom roles must be of the format
        /// `[projects|organizations]/{parent-name}/roles/{role-name}`.
        /// </summary>
        [Output("role")]
        public Output<string> Role { get; private set; } = null!;

        /// <summary>
        /// A reference to the zone where the machine resides. Used to find the parent resource to bind the IAM policy to. If not specified,
        /// the value will be parsed from the identifier of the parent resource. If no zone is provided in the parent identifier and no
        /// zone is specified, it is taken from the provider configuration.
        /// </summary>
        [Output("zone")]
        public Output<string> Zone { get; private set; } = null!;


        /// <summary>
        /// Create a InstanceIAMMember resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public InstanceIAMMember(string name, InstanceIAMMemberArgs args, CustomResourceOptions? options = null)
            : base("gcp:compute/instanceIAMMember:InstanceIAMMember", name, args ?? new InstanceIAMMemberArgs(), MakeResourceOptions(options, ""))
        {
        }

        private InstanceIAMMember(string name, Input<string> id, InstanceIAMMemberState? state = null, CustomResourceOptions? options = null)
            : base("gcp:compute/instanceIAMMember:InstanceIAMMember", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing InstanceIAMMember resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static InstanceIAMMember Get(string name, Input<string> id, InstanceIAMMemberState? state = null, CustomResourceOptions? options = null)
        {
            return new InstanceIAMMember(name, id, state, options);
        }
    }

    public sealed class InstanceIAMMemberArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ) An [IAM Condition](https://cloud.google.com/iam/docs/conditions-overview) for a given binding.
        /// Structure is documented below.
        /// </summary>
        [Input("condition")]
        public Input<Inputs.InstanceIAMMemberConditionArgs>? Condition { get; set; }

        /// <summary>
        /// Used to find the parent resource to bind the IAM policy to
        /// </summary>
        [Input("instanceName", required: true)]
        public Input<string> InstanceName { get; set; } = null!;

        [Input("member", required: true)]
        public Input<string> Member { get; set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// The role that should be applied. Only one
        /// `gcp.compute.InstanceIAMBinding` can be used per role. Note that custom roles must be of the format
        /// `[projects|organizations]/{parent-name}/roles/{role-name}`.
        /// </summary>
        [Input("role", required: true)]
        public Input<string> Role { get; set; } = null!;

        /// <summary>
        /// A reference to the zone where the machine resides. Used to find the parent resource to bind the IAM policy to. If not specified,
        /// the value will be parsed from the identifier of the parent resource. If no zone is provided in the parent identifier and no
        /// zone is specified, it is taken from the provider configuration.
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public InstanceIAMMemberArgs()
        {
        }
    }

    public sealed class InstanceIAMMemberState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ) An [IAM Condition](https://cloud.google.com/iam/docs/conditions-overview) for a given binding.
        /// Structure is documented below.
        /// </summary>
        [Input("condition")]
        public Input<Inputs.InstanceIAMMemberConditionGetArgs>? Condition { get; set; }

        /// <summary>
        /// (Computed) The etag of the IAM policy.
        /// </summary>
        [Input("etag")]
        public Input<string>? Etag { get; set; }

        /// <summary>
        /// Used to find the parent resource to bind the IAM policy to
        /// </summary>
        [Input("instanceName")]
        public Input<string>? InstanceName { get; set; }

        [Input("member")]
        public Input<string>? Member { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// The role that should be applied. Only one
        /// `gcp.compute.InstanceIAMBinding` can be used per role. Note that custom roles must be of the format
        /// `[projects|organizations]/{parent-name}/roles/{role-name}`.
        /// </summary>
        [Input("role")]
        public Input<string>? Role { get; set; }

        /// <summary>
        /// A reference to the zone where the machine resides. Used to find the parent resource to bind the IAM policy to. If not specified,
        /// the value will be parsed from the identifier of the parent resource. If no zone is provided in the parent identifier and no
        /// zone is specified, it is taken from the provider configuration.
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public InstanceIAMMemberState()
        {
        }
    }
}
