/* Main Simulation File */

#if defined(__cplusplus)
extern "C" {
#endif

#include "TwoConnectedTanks_model.h"
#include "simulation/solver/events.h"

/* FIXME these defines are ugly and hard to read, why not use direct function pointers instead? */
#define prefixedName_performSimulation TwoConnectedTanks_performSimulation
#define prefixedName_updateContinuousSystem TwoConnectedTanks_updateContinuousSystem
#include <simulation/solver/perform_simulation.c.inc>

#define prefixedName_performQSSSimulation TwoConnectedTanks_performQSSSimulation
#include <simulation/solver/perform_qss_simulation.c.inc>


/* dummy VARINFO and FILEINFO */
const VAR_INFO dummyVAR_INFO = omc_dummyVarInfo;

int TwoConnectedTanks_input_function(DATA *data, threadData_t *threadData)
{
  TRACE_PUSH

  
  TRACE_POP
  return 0;
}

int TwoConnectedTanks_input_function_init(DATA *data, threadData_t *threadData)
{
  TRACE_PUSH

  
  TRACE_POP
  return 0;
}

int TwoConnectedTanks_input_function_updateStartValues(DATA *data, threadData_t *threadData)
{
  TRACE_PUSH

  
  TRACE_POP
  return 0;
}

int TwoConnectedTanks_inputNames(DATA *data, char ** names){
  TRACE_PUSH

  
  TRACE_POP
  return 0;
}

int TwoConnectedTanks_data_function(DATA *data, threadData_t *threadData)
{
  TRACE_PUSH

  TRACE_POP
  return 0;
}

int TwoConnectedTanks_dataReconciliationInputNames(DATA *data, char ** names){
  TRACE_PUSH

  
  TRACE_POP
  return 0;
}

int TwoConnectedTanks_dataReconciliationUnmeasuredVariables(DATA *data, char ** names)
{
  TRACE_PUSH

  
  TRACE_POP
  return 0;
}

int TwoConnectedTanks_output_function(DATA *data, threadData_t *threadData)
{
  TRACE_PUSH

  
  TRACE_POP
  return 0;
}

int TwoConnectedTanks_setc_function(DATA *data, threadData_t *threadData)
{
  TRACE_PUSH

  
  TRACE_POP
  return 0;
}

int TwoConnectedTanks_setb_function(DATA *data, threadData_t *threadData)
{
  TRACE_PUSH

  
  TRACE_POP
  return 0;
}


/*
equation index: 5
type: SIMPLE_ASSIGN
tank1.Qo = max(0.0, if time <= 5.0 then 0.0 else sqrt(tank2.h))
*/
void TwoConnectedTanks_eqFunction_5(DATA *data, threadData_t *threadData)
{
  TRACE_PUSH
  const int equationIndexes[2] = {1,5};
  modelica_boolean tmp0;
  modelica_real tmp1;
  modelica_real tmp2;
  modelica_real tmp3;
  modelica_boolean tmp4;
  modelica_real tmp5;
  tmp1 = 1.0;
  tmp2 = 5.0;
  relationhysteresis(data, &tmp0, data->localData[0]->timeValue, 5.0, tmp1, tmp2, 0, LessEq, LessEqZC);
  tmp4 = (modelica_boolean)tmp0;
  if(tmp4)
  {
    tmp5 = 0.0;
  }
  else
  {
    tmp3 = (data->localData[0]->realVars[0] /* tank2.h STATE(1) */);
    if(!(tmp3 >= 0.0))
    {
      if (data->simulationInfo->noThrowAsserts) {
        FILE_INFO info = {"",0,0,0,0,0};
        infoStreamPrintWithEquationIndexes(LOG_ASSERT, info, 0, equationIndexes, "The following assertion has been violated %sat time %f", initial() ? "during initialization " : "", data->localData[0]->timeValue);
        data->simulationInfo->needToReThrow = 1;
      } else {
        FILE_INFO info = {"",0,0,0,0,0};
        omc_assert_warning(info, "The following assertion has been violated %sat time %f", initial() ? "during initialization " : "", data->localData[0]->timeValue);
        throwStreamPrintWithEquationIndexes(threadData, info, equationIndexes, "Model error: Argument of sqrt(tank2.h) was %g should be >= 0", tmp3);
      }
    }
    tmp5 = sqrt(tmp3);
  }
  (data->localData[0]->realVars[2] /* tank1.Qo variable */) = fmax(0.0,tmp5);
  TRACE_POP
}
/*
equation index: 6
type: SIMPLE_ASSIGN
$DER.tank2.h = (tank1.Qin - tank1.Qo) / tank1.A
*/
void TwoConnectedTanks_eqFunction_6(DATA *data, threadData_t *threadData)
{
  TRACE_PUSH
  const int equationIndexes[2] = {1,6};
  (data->localData[0]->realVars[1] /* der(tank2.h) STATE_DER */) = DIVISION_SIM((data->simulationInfo->realParameter[1] /* tank1.Qin PARAM */) - (data->localData[0]->realVars[2] /* tank1.Qo variable */),(data->simulationInfo->realParameter[0] /* tank1.A PARAM */),"tank1.A",equationIndexes);
  TRACE_POP
}
/*
equation index: 7
type: SIMPLE_ASSIGN
tank2.Q1 = der(tank2.h) * tank2.A
*/
void TwoConnectedTanks_eqFunction_7(DATA *data, threadData_t *threadData)
{
  TRACE_PUSH
  const int equationIndexes[2] = {1,7};
  (data->localData[0]->realVars[3] /* tank2.Q1 variable */) = ((data->localData[0]->realVars[1] /* der(tank2.h) STATE_DER */)) * ((data->simulationInfo->realParameter[2] /* tank2.A PARAM */));
  TRACE_POP
}

OMC_DISABLE_OPT
int TwoConnectedTanks_functionDAE(DATA *data, threadData_t *threadData)
{
  TRACE_PUSH
  int equationIndexes[1] = {0};
#if !defined(OMC_MINIMAL_RUNTIME)
  if (measure_time_flag) rt_tick(SIM_TIMER_DAE);
#endif

  data->simulationInfo->needToIterate = 0;
  data->simulationInfo->discreteCall = 1;
  TwoConnectedTanks_functionLocalKnownVars(data, threadData);
  TwoConnectedTanks_eqFunction_5(data, threadData);

  TwoConnectedTanks_eqFunction_6(data, threadData);

  TwoConnectedTanks_eqFunction_7(data, threadData);
  data->simulationInfo->discreteCall = 0;
  
#if !defined(OMC_MINIMAL_RUNTIME)
  if (measure_time_flag) rt_accumulate(SIM_TIMER_DAE);
#endif
  TRACE_POP
  return 0;
}


int TwoConnectedTanks_functionLocalKnownVars(DATA *data, threadData_t *threadData)
{
  TRACE_PUSH

  
  TRACE_POP
  return 0;
}


/* forwarded equations */
extern void TwoConnectedTanks_eqFunction_5(DATA* data, threadData_t *threadData);
extern void TwoConnectedTanks_eqFunction_6(DATA* data, threadData_t *threadData);

static void functionODE_system0(DATA *data, threadData_t *threadData)
{
  {
    TwoConnectedTanks_eqFunction_5(data, threadData);
    threadData->lastEquationSolved = 5;
  }
  {
    TwoConnectedTanks_eqFunction_6(data, threadData);
    threadData->lastEquationSolved = 6;
  }
}

int TwoConnectedTanks_functionODE(DATA *data, threadData_t *threadData)
{
  TRACE_PUSH
#if !defined(OMC_MINIMAL_RUNTIME)
  if (measure_time_flag) rt_tick(SIM_TIMER_FUNCTION_ODE);
#endif

  
  data->simulationInfo->callStatistics.functionODE++;
  
  TwoConnectedTanks_functionLocalKnownVars(data, threadData);
  functionODE_system0(data, threadData);

#if !defined(OMC_MINIMAL_RUNTIME)
  if (measure_time_flag) rt_accumulate(SIM_TIMER_FUNCTION_ODE);
#endif

  TRACE_POP
  return 0;
}

/* forward the main in the simulation runtime */
extern int _main_SimulationRuntime(int argc, char**argv, DATA *data, threadData_t *threadData);

#include "TwoConnectedTanks_12jac.h"
#include "TwoConnectedTanks_13opt.h"

struct OpenModelicaGeneratedFunctionCallbacks TwoConnectedTanks_callback = {
   (int (*)(DATA *, threadData_t *, void *)) TwoConnectedTanks_performSimulation,    /* performSimulation */
   (int (*)(DATA *, threadData_t *, void *)) TwoConnectedTanks_performQSSSimulation,    /* performQSSSimulation */
   TwoConnectedTanks_updateContinuousSystem,    /* updateContinuousSystem */
   TwoConnectedTanks_callExternalObjectDestructors,    /* callExternalObjectDestructors */
   NULL,    /* initialNonLinearSystem */
   NULL,    /* initialLinearSystem */
   NULL,    /* initialMixedSystem */
   #if !defined(OMC_NO_STATESELECTION)
   TwoConnectedTanks_initializeStateSets,
   #else
   NULL,
   #endif    /* initializeStateSets */
   TwoConnectedTanks_initializeDAEmodeData,
   TwoConnectedTanks_functionODE,
   TwoConnectedTanks_functionAlgebraics,
   TwoConnectedTanks_functionDAE,
   TwoConnectedTanks_functionLocalKnownVars,
   TwoConnectedTanks_input_function,
   TwoConnectedTanks_input_function_init,
   TwoConnectedTanks_input_function_updateStartValues,
   TwoConnectedTanks_data_function,
   TwoConnectedTanks_output_function,
   TwoConnectedTanks_setc_function,
   TwoConnectedTanks_setb_function,
   TwoConnectedTanks_function_storeDelayed,
   TwoConnectedTanks_function_storeSpatialDistribution,
   TwoConnectedTanks_function_initSpatialDistribution,
   TwoConnectedTanks_updateBoundVariableAttributes,
   TwoConnectedTanks_functionInitialEquations,
   1, /* useHomotopy - 0: local homotopy (equidistant lambda), 1: global homotopy (equidistant lambda), 2: new global homotopy approach (adaptive lambda), 3: new local homotopy approach (adaptive lambda)*/
   NULL,
   TwoConnectedTanks_functionRemovedInitialEquations,
   TwoConnectedTanks_updateBoundParameters,
   TwoConnectedTanks_checkForAsserts,
   TwoConnectedTanks_function_ZeroCrossingsEquations,
   TwoConnectedTanks_function_ZeroCrossings,
   TwoConnectedTanks_function_updateRelations,
   TwoConnectedTanks_zeroCrossingDescription,
   TwoConnectedTanks_relationDescription,
   TwoConnectedTanks_function_initSample,
   TwoConnectedTanks_INDEX_JAC_A,
   TwoConnectedTanks_INDEX_JAC_B,
   TwoConnectedTanks_INDEX_JAC_C,
   TwoConnectedTanks_INDEX_JAC_D,
   TwoConnectedTanks_INDEX_JAC_F,
   TwoConnectedTanks_INDEX_JAC_H,
   TwoConnectedTanks_initialAnalyticJacobianA,
   TwoConnectedTanks_initialAnalyticJacobianB,
   TwoConnectedTanks_initialAnalyticJacobianC,
   TwoConnectedTanks_initialAnalyticJacobianD,
   TwoConnectedTanks_initialAnalyticJacobianF,
   TwoConnectedTanks_initialAnalyticJacobianH,
   TwoConnectedTanks_functionJacA_column,
   TwoConnectedTanks_functionJacB_column,
   TwoConnectedTanks_functionJacC_column,
   TwoConnectedTanks_functionJacD_column,
   TwoConnectedTanks_functionJacF_column,
   TwoConnectedTanks_functionJacH_column,
   TwoConnectedTanks_linear_model_frame,
   TwoConnectedTanks_linear_model_datarecovery_frame,
   TwoConnectedTanks_mayer,
   TwoConnectedTanks_lagrange,
   TwoConnectedTanks_pickUpBoundsForInputsInOptimization,
   TwoConnectedTanks_setInputData,
   TwoConnectedTanks_getTimeGrid,
   TwoConnectedTanks_symbolicInlineSystem,
   TwoConnectedTanks_function_initSynchronous,
   TwoConnectedTanks_function_updateSynchronous,
   TwoConnectedTanks_function_equationsSynchronous,
   TwoConnectedTanks_inputNames,
   TwoConnectedTanks_dataReconciliationInputNames,
   TwoConnectedTanks_dataReconciliationUnmeasuredVariables,
   NULL,
   NULL,
   NULL,
   NULL,
   -1,
   NULL,
   NULL,
   -1

};

#define _OMC_LIT_RESOURCE_0_name_data "Complex"
#define _OMC_LIT_RESOURCE_0_dir_data "C:/Users/SHRI/AppData/Roaming/.openmodelica/libraries/Complex 4.0.0+maint.om"
static const MMC_DEFSTRINGLIT(_OMC_LIT_RESOURCE_0_name,7,_OMC_LIT_RESOURCE_0_name_data);
static const MMC_DEFSTRINGLIT(_OMC_LIT_RESOURCE_0_dir,76,_OMC_LIT_RESOURCE_0_dir_data);

#define _OMC_LIT_RESOURCE_1_name_data "Modelica"
#define _OMC_LIT_RESOURCE_1_dir_data "C:/Users/SHRI/AppData/Roaming/.openmodelica/libraries/Modelica 4.0.0+maint.om"
static const MMC_DEFSTRINGLIT(_OMC_LIT_RESOURCE_1_name,8,_OMC_LIT_RESOURCE_1_name_data);
static const MMC_DEFSTRINGLIT(_OMC_LIT_RESOURCE_1_dir,77,_OMC_LIT_RESOURCE_1_dir_data);

#define _OMC_LIT_RESOURCE_2_name_data "ModelicaServices"
#define _OMC_LIT_RESOURCE_2_dir_data "C:/Users/SHRI/AppData/Roaming/.openmodelica/libraries/ModelicaServices 4.0.0+maint.om"
static const MMC_DEFSTRINGLIT(_OMC_LIT_RESOURCE_2_name,16,_OMC_LIT_RESOURCE_2_name_data);
static const MMC_DEFSTRINGLIT(_OMC_LIT_RESOURCE_2_dir,85,_OMC_LIT_RESOURCE_2_dir_data);

#define _OMC_LIT_RESOURCE_3_name_data "NonInteractingTanks"
#define _OMC_LIT_RESOURCE_3_dir_data "D:/SHRI1/github/OpenModelica-GUI/NonInteractingTanks"
static const MMC_DEFSTRINGLIT(_OMC_LIT_RESOURCE_3_name,19,_OMC_LIT_RESOURCE_3_name_data);
static const MMC_DEFSTRINGLIT(_OMC_LIT_RESOURCE_3_dir,52,_OMC_LIT_RESOURCE_3_dir_data);

static const MMC_DEFSTRUCTLIT(_OMC_LIT_RESOURCES,8,MMC_ARRAY_TAG) {MMC_REFSTRINGLIT(_OMC_LIT_RESOURCE_0_name), MMC_REFSTRINGLIT(_OMC_LIT_RESOURCE_0_dir), MMC_REFSTRINGLIT(_OMC_LIT_RESOURCE_1_name), MMC_REFSTRINGLIT(_OMC_LIT_RESOURCE_1_dir), MMC_REFSTRINGLIT(_OMC_LIT_RESOURCE_2_name), MMC_REFSTRINGLIT(_OMC_LIT_RESOURCE_2_dir), MMC_REFSTRINGLIT(_OMC_LIT_RESOURCE_3_name), MMC_REFSTRINGLIT(_OMC_LIT_RESOURCE_3_dir)}};
void TwoConnectedTanks_setupDataStruc(DATA *data, threadData_t *threadData)
{
  assertStreamPrint(threadData,0!=data, "Error while initialize Data");
  threadData->localRoots[LOCAL_ROOT_SIMULATION_DATA] = data;
  data->callback = &TwoConnectedTanks_callback;
  OpenModelica_updateUriMapping(threadData, MMC_REFSTRUCTLIT(_OMC_LIT_RESOURCES));
  data->modelData->modelName = "NonInteractingTanks.TwoConnectedTanks";
  data->modelData->modelFilePrefix = "TwoConnectedTanks";
  data->modelData->resultFileName = NULL;
  data->modelData->modelDir = "D:/SHRI1/github/OpenModelica-GUI/NonInteractingTanks";
  data->modelData->modelGUID = "{bf4108b6-da96-4748-a97a-af178a3a4e0d}";
  #if defined(OPENMODELICA_XML_FROM_FILE_AT_RUNTIME)
  data->modelData->initXMLData = NULL;
  data->modelData->modelDataXml.infoXMLData = NULL;
  #else
  #if defined(_MSC_VER) /* handle joke compilers */
  {
  /* for MSVC we encode a string like char x[] = {'a', 'b', 'c', '\0'} */
  /* because the string constant limit is 65535 bytes */
  static const char contents_init[] =
    #include "TwoConnectedTanks_init.c"
    ;
  static const char contents_info[] =
    #include "TwoConnectedTanks_info.c"
    ;
    data->modelData->initXMLData = contents_init;
    data->modelData->modelDataXml.infoXMLData = contents_info;
  }
  #else /* handle real compilers */
  data->modelData->initXMLData =
  #include "TwoConnectedTanks_init.c"
    ;
  data->modelData->modelDataXml.infoXMLData =
  #include "TwoConnectedTanks_info.c"
    ;
  #endif /* defined(_MSC_VER) */
  #endif /* defined(OPENMODELICA_XML_FROM_FILE_AT_RUNTIME) */
  data->modelData->modelDataXml.fileName = "TwoConnectedTanks_info.json";
  data->modelData->resourcesDir = NULL;
  data->modelData->runTestsuite = 0;
  data->modelData->nStates = 1;
  data->modelData->nVariablesReal = 4;
  data->modelData->nDiscreteReal = 0;
  data->modelData->nVariablesInteger = 0;
  data->modelData->nVariablesBoolean = 0;
  data->modelData->nVariablesString = 0;
  data->modelData->nParametersReal = 4;
  data->modelData->nParametersInteger = 0;
  data->modelData->nParametersBoolean = 0;
  data->modelData->nParametersString = 0;
  data->modelData->nInputVars = 0;
  data->modelData->nOutputVars = 0;
  data->modelData->nAliasReal = 5;
  data->modelData->nAliasInteger = 0;
  data->modelData->nAliasBoolean = 0;
  data->modelData->nAliasString = 0;
  data->modelData->nZeroCrossings = 1;
  data->modelData->nSamples = 0;
  data->modelData->nRelations = 1;
  data->modelData->nMathEvents = 0;
  data->modelData->nExtObjs = 0;
  data->modelData->modelDataXml.modelInfoXmlLength = 0;
  data->modelData->modelDataXml.nFunctions = 0;
  data->modelData->modelDataXml.nProfileBlocks = 0;
  data->modelData->modelDataXml.nEquations = 8;
  data->modelData->nMixedSystems = 0;
  data->modelData->nLinearSystems = 0;
  data->modelData->nNonLinearSystems = 0;
  data->modelData->nStateSets = 0;
  data->modelData->nJacobians = 6;
  data->modelData->nOptimizeConstraints = 0;
  data->modelData->nOptimizeFinalConstraints = 0;
  data->modelData->nDelayExpressions = 0;
  data->modelData->nBaseClocks = 0;
  data->modelData->nSpatialDistributions = 0;
  data->modelData->nSensitivityVars = 0;
  data->modelData->nSensitivityParamVars = 0;
  data->modelData->nSetcVars = 0;
  data->modelData->ndataReconVars = 0;
  data->modelData->nSetbVars = 0;
  data->modelData->nRelatedBoundaryConditions = 0;
  data->modelData->linearizationDumpLanguage = OMC_LINEARIZE_DUMP_LANGUAGE_MODELICA;
}

static int rml_execution_failed()
{
  fflush(NULL);
  fprintf(stderr, "Execution failed!\n");
  fflush(NULL);
  return 1;
}


#if defined(__MINGW32__) || defined(_MSC_VER)

#if !defined(_UNICODE)
#define _UNICODE
#endif
#if !defined(UNICODE)
#define UNICODE
#endif

#include <windows.h>
char** omc_fixWindowsArgv(int argc, wchar_t **wargv)
{
  char** newargv;
  /* Support for non-ASCII characters
  * Read the unicode command line arguments and translate it to char*
  */
  newargv = (char**)malloc(argc*sizeof(char*));
  for (int i = 0; i < argc; i++) {
    newargv[i] = omc_wchar_to_multibyte_str(wargv[i]);
  }
  return newargv;
}

#define OMC_MAIN wmain
#define OMC_CHAR wchar_t
#define OMC_EXPORT __declspec(dllexport) extern

#else
#define omc_fixWindowsArgv(N, A) (A)
#define OMC_MAIN main
#define OMC_CHAR char
#define OMC_EXPORT extern
#endif

#if defined(threadData)
#undef threadData
#endif
/* call the simulation runtime main from our main! */
#if defined(OMC_DLL_MAIN_DEFINE)
OMC_EXPORT int omcDllMain(int argc, OMC_CHAR **argv)
#else
int OMC_MAIN(int argc, OMC_CHAR** argv)
#endif
{
  char** newargv = omc_fixWindowsArgv(argc, argv);
  /*
    Set the error functions to be used for simulation.
    The default value for them is 'functions' version. Change it here to 'simulation' versions
  */
  omc_assert = omc_assert_simulation;
  omc_assert_withEquationIndexes = omc_assert_simulation_withEquationIndexes;

  omc_assert_warning_withEquationIndexes = omc_assert_warning_simulation_withEquationIndexes;
  omc_assert_warning = omc_assert_warning_simulation;
  omc_terminate = omc_terminate_simulation;
  omc_throw = omc_throw_simulation;

  int res;
  DATA data;
  MODEL_DATA modelData;
  SIMULATION_INFO simInfo;
  data.modelData = &modelData;
  data.simulationInfo = &simInfo;
  measure_time_flag = 0;
  compiledInDAEMode = 0;
  compiledWithSymSolver = 0;
  MMC_INIT(0);
  omc_alloc_interface.init();
  {
    MMC_TRY_TOP()
  
    MMC_TRY_STACK()
  
    TwoConnectedTanks_setupDataStruc(&data, threadData);
    res = _main_initRuntimeAndSimulation(argc, newargv, &data, threadData);
    if(res == 0) {
      res = _main_SimulationRuntime(argc, newargv, &data, threadData);
    }
    
    MMC_ELSE()
    rml_execution_failed();
    fprintf(stderr, "Stack overflow detected and was not caught.\nSend us a bug report at https://trac.openmodelica.org/OpenModelica/newticket\n    Include the following trace:\n");
    printStacktraceMessages();
    fflush(NULL);
    return 1;
    MMC_CATCH_STACK()
    
    MMC_CATCH_TOP(return rml_execution_failed());
  }

  fflush(NULL);
  return res;
}

#ifdef __cplusplus
}
#endif


