within NonInteractingTanks;

connector FlowConnect
  Real P;      // Potential variable
  flow Real F; //defining flow var to fix imbalance error
  annotation(
    Icon(graphics = {Ellipse(origin = {-6.09, -1.69}, fillPattern = FillPattern.Solid, extent = {{-85.91, 97.69}, {85.91, -97.69}}, endAngle = 360)}));
end FlowConnect;
