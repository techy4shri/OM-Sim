/* Algebraic */
#include "TwoConnectedTanks_model.h"

#ifdef __cplusplus
extern "C" {
#endif


/* forwarded equations */
extern void TwoConnectedTanks_eqFunction_7(DATA* data, threadData_t *threadData);

static void functionAlg_system0(DATA *data, threadData_t *threadData)
{
  {
    TwoConnectedTanks_eqFunction_7(data, threadData);
    threadData->lastEquationSolved = 7;
  }
}
/* for continuous time variables */
int TwoConnectedTanks_functionAlgebraics(DATA *data, threadData_t *threadData)
{
  TRACE_PUSH

#if !defined(OMC_MINIMAL_RUNTIME)
  if (measure_time_flag) rt_tick(SIM_TIMER_ALGEBRAICS);
#endif
  data->simulationInfo->callStatistics.functionAlgebraics++;

  TwoConnectedTanks_function_savePreSynchronous(data, threadData);
  
  functionAlg_system0(data, threadData);

#if !defined(OMC_MINIMAL_RUNTIME)
  if (measure_time_flag) rt_accumulate(SIM_TIMER_ALGEBRAICS);
#endif

  TRACE_POP
  return 0;
}

#ifdef __cplusplus
}
#endif
