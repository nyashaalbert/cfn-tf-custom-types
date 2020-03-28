# Terraform::Google::BinaryAuthorizationPolicy

A policy for container image binary authorization.


To get more information about Policy, see:

* [API documentation](https://cloud.google.com/binary-authorization/docs/reference/rest/)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/binary-authorization/)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::BinaryAuthorizationPolicy",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#globalpolicyevaluationmode" title="GlobalPolicyEvaluationMode">GlobalPolicyEvaluationMode</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#admissionwhitelistpatterns" title="AdmissionWhitelistPatterns">AdmissionWhitelistPatterns</a>" : <i>[ <a href="admissionwhitelistpatterns.md">AdmissionWhitelistPatterns</a>, ... ]</i>,
        "<a href="#clusteradmissionrules" title="ClusterAdmissionRules">ClusterAdmissionRules</a>" : <i>[ <a href="clusteradmissionrules.md">ClusterAdmissionRules</a>, ... ]</i>,
        "<a href="#defaultadmissionrule" title="DefaultAdmissionRule">DefaultAdmissionRule</a>" : <i>[ <a href="defaultadmissionrule.md">DefaultAdmissionRule</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::BinaryAuthorizationPolicy
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#globalpolicyevaluationmode" title="GlobalPolicyEvaluationMode">GlobalPolicyEvaluationMode</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#admissionwhitelistpatterns" title="AdmissionWhitelistPatterns">AdmissionWhitelistPatterns</a>: <i>
      - <a href="admissionwhitelistpatterns.md">AdmissionWhitelistPatterns</a></i>
    <a href="#clusteradmissionrules" title="ClusterAdmissionRules">ClusterAdmissionRules</a>: <i>
      - <a href="clusteradmissionrules.md">ClusterAdmissionRules</a></i>
    <a href="#defaultadmissionrule" title="DefaultAdmissionRule">DefaultAdmissionRule</a>: <i>
      - <a href="defaultadmissionrule.md">DefaultAdmissionRule</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlobalPolicyEvaluationMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdmissionWhitelistPatterns

_Required_: No

_Type_: List of <a href="admissionwhitelistpatterns.md">AdmissionWhitelistPatterns</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterAdmissionRules

_Required_: No

_Type_: List of <a href="clusteradmissionrules.md">ClusterAdmissionRules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAdmissionRule

_Required_: No

_Type_: List of <a href="defaultadmissionrule.md">DefaultAdmissionRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.
