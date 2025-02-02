within NonInteractingTanks;

model Tank
parameter Real Qin = 2, A =1;
Real h(start = 1), Qo;
  FlowConnect flowConnect annotation(
    Placement(visible = true, transformation(origin = {18, -8}, extent = {{-10, -10}, {10, 10}}, rotation = 0), iconTransformation(origin = {16, -6}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
flowConnect.F = Qo;
 // Setting a positive initial value for h
equation
// Assigning potential variable (height/pressure)
  flowConnect.P = h;
der(h) = (Qin - Qo)/A;
Qo = max(0, if time <= 5 then 0 else sqrt(h));

// Ensure h remains non-negative
//assert(h >= 0, "Error: Tank height (h) must be non-negative!");
annotation(
    Icon(graphics = {Line(origin = {-7, 10}, points = {{-33, 28}, {-33, -28}, {33, -28}, {33, 28}, {33, 28}}), Line(origin = {-54, 47}, points = {{-24, 7}, {24, 7}, {24, -7}}), Line(origin = {-30, 43.416}, points = {{-4, 2.58397}, {0, -3.41603}, {4, 2.58397}}), Text(origin = {-61, 47}, extent = {{-45, 25}, {-25, -9}}, textString = "Qin"), Text(textColor = {0, 0, 255}, extent = {{0, 30}, {50, 80}}, textString = "%name")}));
end Tank;
