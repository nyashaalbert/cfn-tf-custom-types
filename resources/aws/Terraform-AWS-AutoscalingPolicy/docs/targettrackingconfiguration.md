# Terraform::AWS::AutoscalingPolicy TargetTrackingConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disablescalein" title="DisableScaleIn">DisableScaleIn</a>" : <i>Boolean</i>,
    "<a href="#targetvalue" title="TargetValue">TargetValue</a>" : <i>Double</i>,
    "<a href="#customizedmetricspecification" title="CustomizedMetricSpecification">CustomizedMetricSpecification</a>" : <i>[ <a href="targettrackingconfiguration-customizedmetricspecification.md">CustomizedMetricSpecification</a>, ... ]</i>,
    "<a href="#predefinedmetricspecification" title="PredefinedMetricSpecification">PredefinedMetricSpecification</a>" : <i>[ <a href="targettrackingconfiguration-predefinedmetricspecification.md">PredefinedMetricSpecification</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disablescalein" title="DisableScaleIn">DisableScaleIn</a>: <i>Boolean</i>
<a href="#targetvalue" title="TargetValue">TargetValue</a>: <i>Double</i>
<a href="#customizedmetricspecification" title="CustomizedMetricSpecification">CustomizedMetricSpecification</a>: <i>
      - <a href="targettrackingconfiguration-customizedmetricspecification.md">CustomizedMetricSpecification</a></i>
<a href="#predefinedmetricspecification" title="PredefinedMetricSpecification">PredefinedMetricSpecification</a>: <i>
      - <a href="targettrackingconfiguration-predefinedmetricspecification.md">PredefinedMetricSpecification</a></i>
</pre>

## Properties

#### DisableScaleIn

Indicates whether scale in by the target tracking policy is disabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetValue

The target value for the metric.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomizedMetricSpecification

_Required_: No

_Type_: List of <a href="targettrackingconfiguration-customizedmetricspecification.md">CustomizedMetricSpecification</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PredefinedMetricSpecification

_Required_: No

_Type_: List of <a href="targettrackingconfiguration-predefinedmetricspecification.md">PredefinedMetricSpecification</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
