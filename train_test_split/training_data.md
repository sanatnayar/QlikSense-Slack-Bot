## intent:greet
- good morning
- hello
- hey
- hi

## intent:retrieve
- Can I see the [custom resource](cluster_element)
- display the [CR](cluster_element)
- Can I see the [spec](cluster_element)
- I want to see the [spec](cluster_element)
- want to see the [CR](cluster_element)
- show the [CR](cluster_element)
- Show me [all](cluster_element) my configs
- Can I see a [list](cluster_element) of my contexts
- show me the qliksense operator [custom resource definition](cluster_element)
- show the [custom resource](cluster_element)
- I wanted to see my [CR](cluster_element)
- display the [spec](cluster_element)

## intent:tutorial
- Can I know more about [kubernetes] (technology)
- I want some resources to learn more about [gke] (technology)
- How can I learn more about

## intent:inputKey
- Change attribute [StorageClass](key)
- [StorageClass](key)
- [NameSpace](key)
- Change attribute [Profile](key)
- [ManifestsRoot](key)
- [RotateKeys](key)
- [Profile](key)
- Change attribute [ManifestsRoot](key)

## intent:inputValue
- [eks](value)
- [aws](value)

## intent:setConfig
- i want to edit my cr
- add to my cr spec
- i want to change to my spec
- i want to change my cr
- set an attribute
- I wish to add to my spec

## intent:doPreflight
- check qliksense before deploying
- do all preflight checks
- will qliksense deploy properly?
- do the [deployments](preflight) preflight check
- do all checks before deployment
- check all preflight

## intent:goodbye
- see you around
- see you later
- goodbye

## intent:affirm
- correct
- indeed
- that sounds good
- of course

## intent:deny
- no way
- no
- not really
- never

## intent:bot_challenge
- am I talking to a bot?
- are you a human?
- are you a bot?

## synonym:CR
- custom resource
- spec
- qliksense spec
- deployment custom resource
- deployment spec
- cr

## synonym:CRD
- custom resource definition
- Operator CRD
- operator custom resource definition

## synonym:all
- list

## synonym:deployments
- Dep
- Deployment
- deployment
- dep

## regex:value
- (.*?)

## lookup:cluster_element
  data/tests/element.txt
