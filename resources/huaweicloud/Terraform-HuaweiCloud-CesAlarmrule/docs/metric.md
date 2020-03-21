# Terraform::HuaweiCloud::CesAlarmrule Metric

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#metricname" title="MetricName">MetricName</a>" : <i>String</i>,
    "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
    "<a href="#dimensions" title="Dimensions">Dimensions</a>" : <i>[ <a href="metric-dimensions.md">Dimensions</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#metricname" title="MetricName">MetricName</a>: <i>String</i>
<a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
<a href="#dimensions" title="Dimensions">Dimensions</a>: <i>
      - <a href="metric-dimensions.md">Dimensions</a></i>
</pre>

## Properties

#### MetricName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dimensions

_Required_: No

_Type_: List of <a href="metric-dimensions.md">Dimensions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
