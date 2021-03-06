module Negate4 (input [3:0] I, output [3:0] O);
wire [3:0] inst0_out;
coreir_neg inst0 (.in(I), .out(inst0_out));
assign O = inst0_out;
endmodule

module TestsCircuit_neg_4_UInt_UIntType (input [3:0] I, output [3:0] O0, output [3:0] O1);
wire [3:0] inst0_O;
wire [3:0] inst1_O;
Negate4 inst0 (.I(I), .O(inst0_O));
Negate4 inst1 (.I(I), .O(inst1_O));
assign O0 = inst0_O;
assign O1 = inst1_O;
endmodule

