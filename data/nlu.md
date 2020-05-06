## intent:greet
- hello
- hi
- good morning
- good evening
- hey

## lookup:cluster_element
   data/tests/element.txt
## intent:retrieve
 - I wanted to see my [CR](cluster_element)
 - Can I see the [custom resource](cluster_element)
 - Can I see the qliksense operator [CRD](cluster_element)
 - Can I see a [list](cluster_element) of my contexts
 - I want to see [all](cluster_element) my contexts
 - Show me [all](cluster_element) my configs
 - Can I see the [spec](cluster_element) 
 - show me the [deployment spec](cluster_element)
 - show me the qliksense operator [custom resource definition](cluster_element)
 - want to see the [CR](cluster_element)
 - show me the [custom resource](cluster_element)
 - I want to see the [spec](cluster_element)
 - show the [CR](cluster_element)
 - display the [CR](cluster_element)
 - display the [spec](cluster_element)
 - show the [custom resource](cluster_element)


## intent:tutorial
 - Can I know more about [kubernetes] (technology)
 - I want some resources to learn more about [gke] (technology)
 - what is a [custom resource] (technology)
 - How can I learn more about 

## intent: inputKey
 - [ManifestsRoot](key)
 - [RotateKeys](key)
 - [StorageClass](key)
 - [NameSpace](key)
 - [Profile](key)
 - Change attribute [ManifestsRoot](key)
 - Change attribute [RotateKeys](key)
 - Change attribute [StorageClass](key)
 - Change attribute [NameSpace](key)
 - Change attribute [Profile](key)

 ## intent: inputValue
 - [gcp](value)
 - [aws](value)
 - [eks](value)

## intent: setConfig
 - I wish to add to my spec
 - I want to set an attribute in the custom resource
 - add to my cr spec
 - set an attribute
 - i want to change my cr
 - i want to edit my cr
 - i want to change to my spec
 - i want to edit my spec

## intent: doPreflight
 - check all preflight
 - do all preflight checks
 - do all checks before deployment
 - will qliksense deploy properly?
 - check application before deploying
 - check qliksense before deploying
 - do the [deployments](preflight) preflight check
 - check [deployment](preflight) preflight


## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?


## regex:value
- (.*?)

## synonym:deployments
- Dep
- Deployment
- deployment
- dep


## synonym:CRD
- custom resource definition
- Operator CRD
- operator custom resource definition

## synonym:CR
- custom resource
- spec
- qliksense spec
- deployment custom resource
- deployment spec
- cr

## synonym:all
- list

## intent: notifications
- give me updates on cluster every [5](name) minutes
- update me every [10](name) minutes
- cluster updates every [1](name) minute
- give updates every [20](name) minutes


## intent: EXTERNAL_reminder
- EXTERNAL_reminder
  triggers: action_react_to_reminder

## regex:name
- ([0-9]|[1-5][0-9]|60)

## intent: cancel_notif
- cancel notifications
- please stop the updates
- stop showing logs