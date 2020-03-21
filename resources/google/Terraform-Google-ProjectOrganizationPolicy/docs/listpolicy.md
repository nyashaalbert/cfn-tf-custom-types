# Terraform::Google::ProjectOrganizationPolicy ListPolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#inheritfromparent" title="InheritFromParent">InheritFromParent</a>" : <i>Boolean</i>,
    "<a href="#suggestedvalue" title="SuggestedValue">SuggestedValue</a>" : <i>String</i>,
    "<a href="#allow" title="Allow">Allow</a>" : <i>[ <a href="listpolicy-allow.md">Allow</a>, ... ]</i>,
    "<a href="#deny" title="Deny">Deny</a>" : <i>[ <a href="listpolicy-deny.md">Deny</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#inheritfromparent" title="InheritFromParent">InheritFromParent</a>: <i>Boolean</i>
<a href="#suggestedvalue" title="SuggestedValue">SuggestedValue</a>: <i>String</i>
<a href="#allow" title="Allow">Allow</a>: <i>
      - <a href="listpolicy-allow.md">Allow</a></i>
<a href="#deny" title="Deny">Deny</a>: <i>
      - <a href="listpolicy-deny.md">Deny</a></i>
</pre>

## Properties

#### InheritFromParent

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuggestedValue

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Allow

_Required_: No

_Type_: List of <a href="listpolicy-allow.md">Allow</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Deny

_Required_: No

_Type_: List of <a href="listpolicy-deny.md">Deny</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
