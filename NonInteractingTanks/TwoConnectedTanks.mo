within NonInteractingTanks;

model TwoConnectedTanks
  NonInteractingTanks.Tank2 tank2 annotation(
    Placement(visible = true, transformation(origin = {8, -66}, extent = {{-46, -46}, {46, 46}}, rotation = 0)));
  NonInteractingTanks.Tank tank1 annotation(
    Placement(visible = true, transformation(origin = {-56, -18}, extent = {{-42, -42}, {42, 42}}, rotation = 0)));

equation
  connect(tank1.flowConnect, tank2.flowConnect) annotation(
    Line(points = {{-50, -20}, {-9, -20}, {-9, -50}}));

protected
  annotation(
    Diagram(coordinateSystem(extent = {{-100, 20}, {60, -120}})),
  __OpenModelica_simulationFlags(lv = "LOG_STDOUT,LOG_ASSERT,LOG_STATS", s = "dassl", variableFilter = ".*", maxIntegrationOrder = "3"),
  __OpenModelica_commandLineOptions = "--matchingAlgorithm=PFPlusExt --indexReductionMethod=dynamicStateSelection -d=initialization,NLSanalyticJacobian");

end TwoConnectedTanks;
