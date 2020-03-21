# Terraform::Spotinst::ElastigroupAws

CloudFormation equivalent of spotinst_elastigroup_aws

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Spotinst::ElastigroupAws",
    "Properties" : {
        "<a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#blockdevicesmode" title="BlockDevicesMode">BlockDevicesMode</a>" : <i>String</i>,
        "<a href="#capacityunit" title="CapacityUnit">CapacityUnit</a>" : <i>String</i>,
        "<a href="#cpucredits" title="CpuCredits">CpuCredits</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>" : <i>Double</i>,
        "<a href="#drainingtimeout" title="DrainingTimeout">DrainingTimeout</a>" : <i>Double</i>,
        "<a href="#ebsoptimized" title="EbsOptimized">EbsOptimized</a>" : <i>Boolean</i>,
        "<a href="#elasticips" title="ElasticIps">ElasticIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#elasticloadbalancers" title="ElasticLoadBalancers">ElasticLoadBalancers</a>" : <i>[ String, ... ]</i>,
        "<a href="#enablemonitoring" title="EnableMonitoring">EnableMonitoring</a>" : <i>Boolean</i>,
        "<a href="#fallbacktoondemand" title="FallbackToOndemand">FallbackToOndemand</a>" : <i>Boolean</i>,
        "<a href="#healthcheckgraceperiod" title="HealthCheckGracePeriod">HealthCheckGracePeriod</a>" : <i>Double</i>,
        "<a href="#healthchecktype" title="HealthCheckType">HealthCheckType</a>" : <i>String</i>,
        "<a href="#healthcheckunhealthydurationbeforereplacement" title="HealthCheckUnhealthyDurationBeforeReplacement">HealthCheckUnhealthyDurationBeforeReplacement</a>" : <i>Double</i>,
        "<a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#imageid" title="ImageId">ImageId</a>" : <i>String</i>,
        "<a href="#instancetypesondemand" title="InstanceTypesOndemand">InstanceTypesOndemand</a>" : <i>String</i>,
        "<a href="#instancetypespreferredspot" title="InstanceTypesPreferredSpot">InstanceTypesPreferredSpot</a>" : <i>[ String, ... ]</i>,
        "<a href="#instancetypesspot" title="InstanceTypesSpot">InstanceTypesSpot</a>" : <i>[ String, ... ]</i>,
        "<a href="#keyname" title="KeyName">KeyName</a>" : <i>String</i>,
        "<a href="#lifetimeperiod" title="LifetimePeriod">LifetimePeriod</a>" : <i>String</i>,
        "<a href="#maxsize" title="MaxSize">MaxSize</a>" : <i>Double</i>,
        "<a href="#minsize" title="MinSize">MinSize</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ondemandcount" title="OndemandCount">OndemandCount</a>" : <i>Double</i>,
        "<a href="#orientation" title="Orientation">Orientation</a>" : <i>String</i>,
        "<a href="#persistblockdevices" title="PersistBlockDevices">PersistBlockDevices</a>" : <i>Boolean</i>,
        "<a href="#persistprivateip" title="PersistPrivateIp">PersistPrivateIp</a>" : <i>Boolean</i>,
        "<a href="#persistrootdevice" title="PersistRootDevice">PersistRootDevice</a>" : <i>Boolean</i>,
        "<a href="#placementtenancy" title="PlacementTenancy">PlacementTenancy</a>" : <i>String</i>,
        "<a href="#preferredavailabilityzones" title="PreferredAvailabilityZones">PreferredAvailabilityZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#privateips" title="PrivateIps">PrivateIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#product" title="Product">Product</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#shutdownscript" title="ShutdownScript">ShutdownScript</a>" : <i>String</i>,
        "<a href="#spotpercentage" title="SpotPercentage">SpotPercentage</a>" : <i>Double</i>,
        "<a href="#subnetids" title="SubnetIds">SubnetIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#targetgrouparns" title="TargetGroupArns">TargetGroupArns</a>" : <i>[ String, ... ]</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#utilizereservedinstances" title="UtilizeReservedInstances">UtilizeReservedInstances</a>" : <i>Boolean</i>,
        "<a href="#waitforcapacity" title="WaitForCapacity">WaitForCapacity</a>" : <i>Double</i>,
        "<a href="#waitforcapacitytimeout" title="WaitForCapacityTimeout">WaitForCapacityTimeout</a>" : <i>Double</i>,
        "<a href="#ebsblockdevice" title="EbsBlockDevice">EbsBlockDevice</a>" : <i>[ <a href="ebsblockdevice.md">EbsBlockDevice</a>, ... ]</i>,
        "<a href="#ephemeralblockdevice" title="EphemeralBlockDevice">EphemeralBlockDevice</a>" : <i>[ <a href="ephemeralblockdevice.md">EphemeralBlockDevice</a>, ... ]</i>,
        "<a href="#instancetypesweights" title="InstanceTypesWeights">InstanceTypesWeights</a>" : <i>[ <a href="instancetypesweights.md">InstanceTypesWeights</a>, ... ]</i>,
        "<a href="#integrationbeanstalk" title="IntegrationBeanstalk">IntegrationBeanstalk</a>" : <i>[ <a href="integrationbeanstalk.md">IntegrationBeanstalk</a>, ... ]</i>,
        "<a href="#integrationcodedeploy" title="IntegrationCodedeploy">IntegrationCodedeploy</a>" : <i>[ <a href="integrationcodedeploy.md">IntegrationCodedeploy</a>, ... ]</i>,
        "<a href="#integrationdockerswarm" title="IntegrationDockerSwarm">IntegrationDockerSwarm</a>" : <i>[ <a href="integrationdockerswarm.md">IntegrationDockerSwarm</a>, ... ]</i>,
        "<a href="#integrationecs" title="IntegrationEcs">IntegrationEcs</a>" : <i>[ <a href="integrationecs.md">IntegrationEcs</a>, ... ]</i>,
        "<a href="#integrationgitlab" title="IntegrationGitlab">IntegrationGitlab</a>" : <i>[ <a href="integrationgitlab.md">IntegrationGitlab</a>, ... ]</i>,
        "<a href="#integrationkubernetes" title="IntegrationKubernetes">IntegrationKubernetes</a>" : <i>[ <a href="integrationkubernetes.md">IntegrationKubernetes</a>, ... ]</i>,
        "<a href="#integrationmesosphere" title="IntegrationMesosphere">IntegrationMesosphere</a>" : <i>[ <a href="integrationmesosphere.md">IntegrationMesosphere</a>, ... ]</i>,
        "<a href="#integrationmultairuntime" title="IntegrationMultaiRuntime">IntegrationMultaiRuntime</a>" : <i>[ <a href="integrationmultairuntime.md">IntegrationMultaiRuntime</a>, ... ]</i>,
        "<a href="#integrationnomad" title="IntegrationNomad">IntegrationNomad</a>" : <i>[ <a href="integrationnomad.md">IntegrationNomad</a>, ... ]</i>,
        "<a href="#integrationrancher" title="IntegrationRancher">IntegrationRancher</a>" : <i>[ <a href="integrationrancher.md">IntegrationRancher</a>, ... ]</i>,
        "<a href="#integrationroute53" title="IntegrationRoute53">IntegrationRoute53</a>" : <i>[ <a href="integrationroute53.md">IntegrationRoute53</a>, ... ]</i>,
        "<a href="#multaitargetsets" title="MultaiTargetSets">MultaiTargetSets</a>" : <i>[ <a href="multaitargetsets.md">MultaiTargetSets</a>, ... ]</i>,
        "<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>" : <i>[ <a href="networkinterface.md">NetworkInterface</a>, ... ]</i>,
        "<a href="#reverttospot" title="RevertToSpot">RevertToSpot</a>" : <i>[ <a href="reverttospot.md">RevertToSpot</a>, ... ]</i>,
        "<a href="#scalingdownpolicy" title="ScalingDownPolicy">ScalingDownPolicy</a>" : <i>[ <a href="scalingdownpolicy.md">ScalingDownPolicy</a>, ... ]</i>,
        "<a href="#scalingstrategy" title="ScalingStrategy">ScalingStrategy</a>" : <i>[ <a href="scalingstrategy.md">ScalingStrategy</a>, ... ]</i>,
        "<a href="#scalingtargetpolicy" title="ScalingTargetPolicy">ScalingTargetPolicy</a>" : <i>[ <a href="scalingtargetpolicy.md">ScalingTargetPolicy</a>, ... ]</i>,
        "<a href="#scalinguppolicy" title="ScalingUpPolicy">ScalingUpPolicy</a>" : <i>[ <a href="scalinguppolicy.md">ScalingUpPolicy</a>, ... ]</i>,
        "<a href="#scheduledtask" title="ScheduledTask">ScheduledTask</a>" : <i>[ <a href="scheduledtask.md">ScheduledTask</a>, ... ]</i>,
        "<a href="#signal" title="Signal">Signal</a>" : <i>[ <a href="signal.md">Signal</a>, ... ]</i>,
        "<a href="#statefuldeallocation" title="StatefulDeallocation">StatefulDeallocation</a>" : <i>[ <a href="statefuldeallocation.md">StatefulDeallocation</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#updatepolicy" title="UpdatePolicy">UpdatePolicy</a>" : <i>[ <a href="updatepolicy.md">UpdatePolicy</a>, ... ]</i>,
        "<a href="#deploymentpreferences" title="DeploymentPreferences">DeploymentPreferences</a>" : <i>[ <a href="deploymentpreferences.md">DeploymentPreferences</a>, ... ]</i>,
        "<a href="#managedactions" title="ManagedActions">ManagedActions</a>" : <i>[ <a href="managedactions.md">ManagedActions</a>, ... ]</i>,
        "<a href="#deploymentgroups" title="DeploymentGroups">DeploymentGroups</a>" : <i>[ <a href="deploymentgroups.md">DeploymentGroups</a>, ... ]</i>,
        "<a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>" : <i>[ <a href="autoscaledown.md">AutoscaleDown</a>, ... ]</i>,
        "<a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>" : <i>[ <a href="autoscaleheadroom.md">AutoscaleHeadroom</a>, ... ]</i>,
        "<a href="#autoscaleattributes" title="AutoscaleAttributes">AutoscaleAttributes</a>" : <i>[ <a href="autoscaleattributes.md">AutoscaleAttributes</a>, ... ]</i>,
        "<a href="#runner" title="Runner">Runner</a>" : <i>[ <a href="runner.md">Runner</a>, ... ]</i>,
        "<a href="#autoscalelabels" title="AutoscaleLabels">AutoscaleLabels</a>" : <i>[ <a href="autoscalelabels.md">AutoscaleLabels</a>, ... ]</i>,
        "<a href="#autoscaleconstraints" title="AutoscaleConstraints">AutoscaleConstraints</a>" : <i>[ <a href="autoscaleconstraints.md">AutoscaleConstraints</a>, ... ]</i>,
        "<a href="#domains" title="Domains">Domains</a>" : <i>[ <a href="domains.md">Domains</a>, ... ]</i>,
        "<a href="#dimensions" title="Dimensions">Dimensions</a>" : <i>[ <a href="dimensions.md">Dimensions</a>, ... ]</i>,
        "<a href="#rollconfig" title="RollConfig">RollConfig</a>" : <i>[ <a href="rollconfig.md">RollConfig</a>, ... ]</i>,
        "<a href="#strategy" title="Strategy">Strategy</a>" : <i>[ <a href="strategy.md">Strategy</a>, ... ]</i>,
        "<a href="#platformupdate" title="PlatformUpdate">PlatformUpdate</a>" : <i>[ <a href="platformupdate.md">PlatformUpdate</a>, ... ]</i>,
        "<a href="#recordsets" title="RecordSets">RecordSets</a>" : <i>[ <a href="recordsets.md">RecordSets</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Spotinst::ElastigroupAws
Properties:
    <a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>: <i>
      - String</i>
    <a href="#blockdevicesmode" title="BlockDevicesMode">BlockDevicesMode</a>: <i>String</i>
    <a href="#capacityunit" title="CapacityUnit">CapacityUnit</a>: <i>String</i>
    <a href="#cpucredits" title="CpuCredits">CpuCredits</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#desiredcapacity" title="DesiredCapacity">DesiredCapacity</a>: <i>Double</i>
    <a href="#drainingtimeout" title="DrainingTimeout">DrainingTimeout</a>: <i>Double</i>
    <a href="#ebsoptimized" title="EbsOptimized">EbsOptimized</a>: <i>Boolean</i>
    <a href="#elasticips" title="ElasticIps">ElasticIps</a>: <i>
      - String</i>
    <a href="#elasticloadbalancers" title="ElasticLoadBalancers">ElasticLoadBalancers</a>: <i>
      - String</i>
    <a href="#enablemonitoring" title="EnableMonitoring">EnableMonitoring</a>: <i>Boolean</i>
    <a href="#fallbacktoondemand" title="FallbackToOndemand">FallbackToOndemand</a>: <i>Boolean</i>
    <a href="#healthcheckgraceperiod" title="HealthCheckGracePeriod">HealthCheckGracePeriod</a>: <i>Double</i>
    <a href="#healthchecktype" title="HealthCheckType">HealthCheckType</a>: <i>String</i>
    <a href="#healthcheckunhealthydurationbeforereplacement" title="HealthCheckUnhealthyDurationBeforeReplacement">HealthCheckUnhealthyDurationBeforeReplacement</a>: <i>Double</i>
    <a href="#iaminstanceprofile" title="IamInstanceProfile">IamInstanceProfile</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#imageid" title="ImageId">ImageId</a>: <i>String</i>
    <a href="#instancetypesondemand" title="InstanceTypesOndemand">InstanceTypesOndemand</a>: <i>String</i>
    <a href="#instancetypespreferredspot" title="InstanceTypesPreferredSpot">InstanceTypesPreferredSpot</a>: <i>
      - String</i>
    <a href="#instancetypesspot" title="InstanceTypesSpot">InstanceTypesSpot</a>: <i>
      - String</i>
    <a href="#keyname" title="KeyName">KeyName</a>: <i>String</i>
    <a href="#lifetimeperiod" title="LifetimePeriod">LifetimePeriod</a>: <i>String</i>
    <a href="#maxsize" title="MaxSize">MaxSize</a>: <i>Double</i>
    <a href="#minsize" title="MinSize">MinSize</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ondemandcount" title="OndemandCount">OndemandCount</a>: <i>Double</i>
    <a href="#orientation" title="Orientation">Orientation</a>: <i>String</i>
    <a href="#persistblockdevices" title="PersistBlockDevices">PersistBlockDevices</a>: <i>Boolean</i>
    <a href="#persistprivateip" title="PersistPrivateIp">PersistPrivateIp</a>: <i>Boolean</i>
    <a href="#persistrootdevice" title="PersistRootDevice">PersistRootDevice</a>: <i>Boolean</i>
    <a href="#placementtenancy" title="PlacementTenancy">PlacementTenancy</a>: <i>String</i>
    <a href="#preferredavailabilityzones" title="PreferredAvailabilityZones">PreferredAvailabilityZones</a>: <i>
      - String</i>
    <a href="#privateips" title="PrivateIps">PrivateIps</a>: <i>
      - String</i>
    <a href="#product" title="Product">Product</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - String</i>
    <a href="#shutdownscript" title="ShutdownScript">ShutdownScript</a>: <i>String</i>
    <a href="#spotpercentage" title="SpotPercentage">SpotPercentage</a>: <i>Double</i>
    <a href="#subnetids" title="SubnetIds">SubnetIds</a>: <i>
      - String</i>
    <a href="#targetgrouparns" title="TargetGroupArns">TargetGroupArns</a>: <i>
      - String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#utilizereservedinstances" title="UtilizeReservedInstances">UtilizeReservedInstances</a>: <i>Boolean</i>
    <a href="#waitforcapacity" title="WaitForCapacity">WaitForCapacity</a>: <i>Double</i>
    <a href="#waitforcapacitytimeout" title="WaitForCapacityTimeout">WaitForCapacityTimeout</a>: <i>Double</i>
    <a href="#ebsblockdevice" title="EbsBlockDevice">EbsBlockDevice</a>: <i>
      - <a href="ebsblockdevice.md">EbsBlockDevice</a></i>
    <a href="#ephemeralblockdevice" title="EphemeralBlockDevice">EphemeralBlockDevice</a>: <i>
      - <a href="ephemeralblockdevice.md">EphemeralBlockDevice</a></i>
    <a href="#instancetypesweights" title="InstanceTypesWeights">InstanceTypesWeights</a>: <i>
      - <a href="instancetypesweights.md">InstanceTypesWeights</a></i>
    <a href="#integrationbeanstalk" title="IntegrationBeanstalk">IntegrationBeanstalk</a>: <i>
      - <a href="integrationbeanstalk.md">IntegrationBeanstalk</a></i>
    <a href="#integrationcodedeploy" title="IntegrationCodedeploy">IntegrationCodedeploy</a>: <i>
      - <a href="integrationcodedeploy.md">IntegrationCodedeploy</a></i>
    <a href="#integrationdockerswarm" title="IntegrationDockerSwarm">IntegrationDockerSwarm</a>: <i>
      - <a href="integrationdockerswarm.md">IntegrationDockerSwarm</a></i>
    <a href="#integrationecs" title="IntegrationEcs">IntegrationEcs</a>: <i>
      - <a href="integrationecs.md">IntegrationEcs</a></i>
    <a href="#integrationgitlab" title="IntegrationGitlab">IntegrationGitlab</a>: <i>
      - <a href="integrationgitlab.md">IntegrationGitlab</a></i>
    <a href="#integrationkubernetes" title="IntegrationKubernetes">IntegrationKubernetes</a>: <i>
      - <a href="integrationkubernetes.md">IntegrationKubernetes</a></i>
    <a href="#integrationmesosphere" title="IntegrationMesosphere">IntegrationMesosphere</a>: <i>
      - <a href="integrationmesosphere.md">IntegrationMesosphere</a></i>
    <a href="#integrationmultairuntime" title="IntegrationMultaiRuntime">IntegrationMultaiRuntime</a>: <i>
      - <a href="integrationmultairuntime.md">IntegrationMultaiRuntime</a></i>
    <a href="#integrationnomad" title="IntegrationNomad">IntegrationNomad</a>: <i>
      - <a href="integrationnomad.md">IntegrationNomad</a></i>
    <a href="#integrationrancher" title="IntegrationRancher">IntegrationRancher</a>: <i>
      - <a href="integrationrancher.md">IntegrationRancher</a></i>
    <a href="#integrationroute53" title="IntegrationRoute53">IntegrationRoute53</a>: <i>
      - <a href="integrationroute53.md">IntegrationRoute53</a></i>
    <a href="#multaitargetsets" title="MultaiTargetSets">MultaiTargetSets</a>: <i>
      - <a href="multaitargetsets.md">MultaiTargetSets</a></i>
    <a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>: <i>
      - <a href="networkinterface.md">NetworkInterface</a></i>
    <a href="#reverttospot" title="RevertToSpot">RevertToSpot</a>: <i>
      - <a href="reverttospot.md">RevertToSpot</a></i>
    <a href="#scalingdownpolicy" title="ScalingDownPolicy">ScalingDownPolicy</a>: <i>
      - <a href="scalingdownpolicy.md">ScalingDownPolicy</a></i>
    <a href="#scalingstrategy" title="ScalingStrategy">ScalingStrategy</a>: <i>
      - <a href="scalingstrategy.md">ScalingStrategy</a></i>
    <a href="#scalingtargetpolicy" title="ScalingTargetPolicy">ScalingTargetPolicy</a>: <i>
      - <a href="scalingtargetpolicy.md">ScalingTargetPolicy</a></i>
    <a href="#scalinguppolicy" title="ScalingUpPolicy">ScalingUpPolicy</a>: <i>
      - <a href="scalinguppolicy.md">ScalingUpPolicy</a></i>
    <a href="#scheduledtask" title="ScheduledTask">ScheduledTask</a>: <i>
      - <a href="scheduledtask.md">ScheduledTask</a></i>
    <a href="#signal" title="Signal">Signal</a>: <i>
      - <a href="signal.md">Signal</a></i>
    <a href="#statefuldeallocation" title="StatefulDeallocation">StatefulDeallocation</a>: <i>
      - <a href="statefuldeallocation.md">StatefulDeallocation</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#updatepolicy" title="UpdatePolicy">UpdatePolicy</a>: <i>
      - <a href="updatepolicy.md">UpdatePolicy</a></i>
    <a href="#deploymentpreferences" title="DeploymentPreferences">DeploymentPreferences</a>: <i>
      - <a href="deploymentpreferences.md">DeploymentPreferences</a></i>
    <a href="#managedactions" title="ManagedActions">ManagedActions</a>: <i>
      - <a href="managedactions.md">ManagedActions</a></i>
    <a href="#deploymentgroups" title="DeploymentGroups">DeploymentGroups</a>: <i>
      - <a href="deploymentgroups.md">DeploymentGroups</a></i>
    <a href="#autoscaledown" title="AutoscaleDown">AutoscaleDown</a>: <i>
      - <a href="autoscaledown.md">AutoscaleDown</a></i>
    <a href="#autoscaleheadroom" title="AutoscaleHeadroom">AutoscaleHeadroom</a>: <i>
      - <a href="autoscaleheadroom.md">AutoscaleHeadroom</a></i>
    <a href="#autoscaleattributes" title="AutoscaleAttributes">AutoscaleAttributes</a>: <i>
      - <a href="autoscaleattributes.md">AutoscaleAttributes</a></i>
    <a href="#runner" title="Runner">Runner</a>: <i>
      - <a href="runner.md">Runner</a></i>
    <a href="#autoscalelabels" title="AutoscaleLabels">AutoscaleLabels</a>: <i>
      - <a href="autoscalelabels.md">AutoscaleLabels</a></i>
    <a href="#autoscaleconstraints" title="AutoscaleConstraints">AutoscaleConstraints</a>: <i>
      - <a href="autoscaleconstraints.md">AutoscaleConstraints</a></i>
    <a href="#domains" title="Domains">Domains</a>: <i>
      - <a href="domains.md">Domains</a></i>
    <a href="#dimensions" title="Dimensions">Dimensions</a>: <i>
      - <a href="dimensions.md">Dimensions</a></i>
    <a href="#rollconfig" title="RollConfig">RollConfig</a>: <i>
      - <a href="rollconfig.md">RollConfig</a></i>
    <a href="#strategy" title="Strategy">Strategy</a>: <i>
      - <a href="strategy.md">Strategy</a></i>
    <a href="#platformupdate" title="PlatformUpdate">PlatformUpdate</a>: <i>
      - <a href="platformupdate.md">PlatformUpdate</a></i>
    <a href="#recordsets" title="RecordSets">RecordSets</a>: <i>
      - <a href="recordsets.md">RecordSets</a></i>
</pre>

## Properties

#### AvailabilityZones

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockDevicesMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityUnit

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuCredits

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesiredCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrainingTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsOptimized

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ElasticLoadBalancers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableMonitoring

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FallbackToOndemand

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckGracePeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckUnhealthyDurationBeforeReplacement

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamInstanceProfile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypesOndemand

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypesPreferredSpot

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypesSpot

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifetimePeriod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OndemandCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Orientation

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistBlockDevices

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistPrivateIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistRootDevice

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementTenancy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredAvailabilityZones

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Product

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShutdownScript

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotPercentage

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupArns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UtilizeReservedInstances

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForCapacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForCapacityTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsBlockDevice

_Required_: No

_Type_: List of <a href="ebsblockdevice.md">EbsBlockDevice</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EphemeralBlockDevice

_Required_: No

_Type_: List of <a href="ephemeralblockdevice.md">EphemeralBlockDevice</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTypesWeights

_Required_: No

_Type_: List of <a href="instancetypesweights.md">InstanceTypesWeights</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationBeanstalk

_Required_: No

_Type_: List of <a href="integrationbeanstalk.md">IntegrationBeanstalk</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationCodedeploy

_Required_: No

_Type_: List of <a href="integrationcodedeploy.md">IntegrationCodedeploy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationDockerSwarm

_Required_: No

_Type_: List of <a href="integrationdockerswarm.md">IntegrationDockerSwarm</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationEcs

_Required_: No

_Type_: List of <a href="integrationecs.md">IntegrationEcs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationGitlab

_Required_: No

_Type_: List of <a href="integrationgitlab.md">IntegrationGitlab</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationKubernetes

_Required_: No

_Type_: List of <a href="integrationkubernetes.md">IntegrationKubernetes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationMesosphere

_Required_: No

_Type_: List of <a href="integrationmesosphere.md">IntegrationMesosphere</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationMultaiRuntime

_Required_: No

_Type_: List of <a href="integrationmultairuntime.md">IntegrationMultaiRuntime</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationNomad

_Required_: No

_Type_: List of <a href="integrationnomad.md">IntegrationNomad</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationRancher

_Required_: No

_Type_: List of <a href="integrationrancher.md">IntegrationRancher</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationRoute53

_Required_: No

_Type_: List of <a href="integrationroute53.md">IntegrationRoute53</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultaiTargetSets

_Required_: No

_Type_: List of <a href="multaitargetsets.md">MultaiTargetSets</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterface

_Required_: No

_Type_: List of <a href="networkinterface.md">NetworkInterface</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RevertToSpot

_Required_: No

_Type_: List of <a href="reverttospot.md">RevertToSpot</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingDownPolicy

_Required_: No

_Type_: List of <a href="scalingdownpolicy.md">ScalingDownPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingStrategy

_Required_: No

_Type_: List of <a href="scalingstrategy.md">ScalingStrategy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingTargetPolicy

_Required_: No

_Type_: List of <a href="scalingtargetpolicy.md">ScalingTargetPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScalingUpPolicy

_Required_: No

_Type_: List of <a href="scalinguppolicy.md">ScalingUpPolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScheduledTask

_Required_: No

_Type_: List of <a href="scheduledtask.md">ScheduledTask</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Signal

_Required_: No

_Type_: List of <a href="signal.md">Signal</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatefulDeallocation

_Required_: No

_Type_: List of <a href="statefuldeallocation.md">StatefulDeallocation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdatePolicy

_Required_: No

_Type_: List of <a href="updatepolicy.md">UpdatePolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentPreferences

_Required_: No

_Type_: List of <a href="deploymentpreferences.md">DeploymentPreferences</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedActions

_Required_: No

_Type_: List of <a href="managedactions.md">ManagedActions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentGroups

_Required_: No

_Type_: List of <a href="deploymentgroups.md">DeploymentGroups</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleDown

_Required_: No

_Type_: List of <a href="autoscaledown.md">AutoscaleDown</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleHeadroom

_Required_: No

_Type_: List of <a href="autoscaleheadroom.md">AutoscaleHeadroom</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleAttributes

_Required_: No

_Type_: List of <a href="autoscaleattributes.md">AutoscaleAttributes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Runner

_Required_: No

_Type_: List of <a href="runner.md">Runner</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleLabels

_Required_: No

_Type_: List of <a href="autoscalelabels.md">AutoscaleLabels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleConstraints

_Required_: No

_Type_: List of <a href="autoscaleconstraints.md">AutoscaleConstraints</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domains

_Required_: No

_Type_: List of <a href="domains.md">Domains</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dimensions

_Required_: No

_Type_: List of <a href="dimensions.md">Dimensions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RollConfig

_Required_: No

_Type_: List of <a href="rollconfig.md">RollConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Strategy

_Required_: No

_Type_: List of <a href="strategy.md">Strategy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlatformUpdate

_Required_: No

_Type_: List of <a href="platformupdate.md">PlatformUpdate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecordSets

_Required_: No

_Type_: List of <a href="recordsets.md">RecordSets</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.
