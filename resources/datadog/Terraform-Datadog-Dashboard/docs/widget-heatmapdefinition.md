# Terraform::Datadog::Dashboard Widget HeatmapDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#time" title="Time">Time</a>" : <i>[ <a href="widget-heatmapdefinition-time.md">Time</a>, ... ]</i>,
    "<a href="#title" title="Title">Title</a>" : <i>String</i>,
    "<a href="#titlealign" title="TitleAlign">TitleAlign</a>" : <i>String</i>,
    "<a href="#titlesize" title="TitleSize">TitleSize</a>" : <i>String</i>,
    "<a href="#request" title="Request">Request</a>" : <i>[ <a href="widget-heatmapdefinition-request.md">Request</a>, ... ]</i>,
    "<a href="#yaxis" title="Yaxis">Yaxis</a>" : <i>[ <a href="widget-heatmapdefinition-yaxis.md">Yaxis</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#time" title="Time">Time</a>: <i>
      - <a href="widget-heatmapdefinition-time.md">Time</a></i>
<a href="#title" title="Title">Title</a>: <i>String</i>
<a href="#titlealign" title="TitleAlign">TitleAlign</a>: <i>String</i>
<a href="#titlesize" title="TitleSize">TitleSize</a>: <i>String</i>
<a href="#request" title="Request">Request</a>: <i>
      - <a href="widget-heatmapdefinition-request.md">Request</a></i>
<a href="#yaxis" title="Yaxis">Yaxis</a>: <i>
      - <a href="widget-heatmapdefinition-yaxis.md">Yaxis</a></i>
</pre>

## Properties

#### Time

_Required_: No

_Type_: List of <a href="widget-heatmapdefinition-time.md">Time</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TitleAlign

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TitleSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Request

_Required_: No

_Type_: List of <a href="widget-heatmapdefinition-request.md">Request</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Yaxis

_Required_: No

_Type_: List of <a href="widget-heatmapdefinition-yaxis.md">Yaxis</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
