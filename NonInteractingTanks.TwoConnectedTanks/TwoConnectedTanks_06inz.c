/* Initialization */
#include "TwoConnectedTanks_model.h"
#include "TwoConnectedTanks_11mix.h"
#include "TwoConnectedTanks_12jac.h"
#if defined(__cplusplus)
extern "C" {
#endif

void TwoConnectedTanks_functionInitialEquations_0(DATA *data, threadData_t *threadData);

/*
equation index: 1
type: SIMPLE_ASSIGN
tank2.h = $START.tank2.h
*/
void TwoConnectedTanks_eqFunction_1(DATA *data, threadData_t *threadData)
{
  TRACE_PUSH
  const int equationIndexes[2] = {1,1};
  (data->localData[0]->realVars[0] /* tank2.h STATE(1) */) = (data->modelData->realVarsData[0] /* tank2.h STATE(1) */).attribute .start;
  TRACE_POP
}
extern void TwoConnectedTanks_eqFunction_5(DATA *data, threadData_t *threadData);

extern void TwoConnectedTanks_eqFunction_6(DATA *data, threadData_t *threadData);


/*
equation index: 4
type: SIMPLE_ASSIGN
tank2.Q1 = $DER.tank2.h * tank2.A
*/
void TwoConnectedTanks_eqFunction_4(DATA *data, threadData_t *threadData)
{
  TRACE_PUSH
  const int equationIndexes[2] = {1,4};
  (data->localData[0]->realVars[3] /* tank2.Q1 variable */) = ((data->localData[0]->realVars[1] /* der(tank2.h) STATE_DER */)) * ((data->simulationInfo->realParameter[2] /* tank2.A PARAM */));
  TRACE_POP
}
OMC_DISABLE_OPT
void TwoConnectedTanks_functionInitialEquations_0(DATA *data, threadData_t *threadData)
{
  TRACE_PUSH
  TwoConnectedTanks_eqFunction_1(data, threadData);
  TwoConnectedTanks_eqFunction_5(data, threadData);
  TwoConnectedTanks_eqFunction_6(data, threadData);
  TwoConnectedTanks_eqFunction_4(data, threadData);
  TRACE_POP
}

int TwoConnectedTanks_functionInitialEquations(DATA *data, threadData_t *threadData)
{
  TRACE_PUSH

  data->simulationInfo->discreteCall = 1;
  TwoConnectedTanks_functionInitialEquations_0(data, threadData);
  data->simulationInfo->discreteCall = 0;
  
  TRACE_POP
  return 0;
}

/* No TwoConnectedTanks_functionInitialEquations_lambda0 function */

int TwoConnectedTanks_functionRemovedInitialEquations(DATA *data, threadData_t *threadData)
{
  TRACE_PUSH
  const int *equationIndexes = NULL;
  double res = 0.0;

  
  TRACE_POP
  return 0;
}


#if defined(__cplusplus)
}
#endif

