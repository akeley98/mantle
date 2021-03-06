module Add8_cout (input [7:0] I0, input [7:0] I1, output [7:0] O, output  COUT);
wire  inst0_O5;
wire  inst0_O6;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O5;
wire  inst3_O6;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O5;
wire  inst6_O6;
wire  inst7_O;
wire  inst8_O;
wire  inst9_O5;
wire  inst9_O6;
wire  inst10_O;
wire  inst11_O;
wire  inst12_O5;
wire  inst12_O6;
wire  inst13_O;
wire  inst14_O;
wire  inst15_O5;
wire  inst15_O6;
wire  inst16_O;
wire  inst17_O;
wire  inst18_O5;
wire  inst18_O6;
wire  inst19_O;
wire  inst20_O;
wire  inst21_O5;
wire  inst21_O6;
wire  inst22_O;
wire  inst23_O;
LUT6_2 #(.INIT(64'h66666666AAAAAAAA)) inst0 (.I0(I0[0]), .I1(I1[0]), .I2(1'b0), .I3(1'b0), .I4(1'b0), .I5(1'b1), .O5(inst0_O5), .O6(inst0_O6));
MUXCY inst1 (.DI(inst0_O5), .CI(1'b0), .S(inst0_O6), .O(inst1_O));
XORCY inst2 (.LI(inst0_O6), .CI(1'b0), .O(inst2_O));
LUT6_2 #(.INIT(64'h66666666AAAAAAAA)) inst3 (.I0(I0[1]), .I1(I1[1]), .I2(1'b0), .I3(1'b0), .I4(1'b0), .I5(1'b1), .O5(inst3_O5), .O6(inst3_O6));
MUXCY inst4 (.DI(inst3_O5), .CI(inst1_O), .S(inst3_O6), .O(inst4_O));
XORCY inst5 (.LI(inst3_O6), .CI(inst1_O), .O(inst5_O));
LUT6_2 #(.INIT(64'h66666666AAAAAAAA)) inst6 (.I0(I0[2]), .I1(I1[2]), .I2(1'b0), .I3(1'b0), .I4(1'b0), .I5(1'b1), .O5(inst6_O5), .O6(inst6_O6));
MUXCY inst7 (.DI(inst6_O5), .CI(inst4_O), .S(inst6_O6), .O(inst7_O));
XORCY inst8 (.LI(inst6_O6), .CI(inst4_O), .O(inst8_O));
LUT6_2 #(.INIT(64'h66666666AAAAAAAA)) inst9 (.I0(I0[3]), .I1(I1[3]), .I2(1'b0), .I3(1'b0), .I4(1'b0), .I5(1'b1), .O5(inst9_O5), .O6(inst9_O6));
MUXCY inst10 (.DI(inst9_O5), .CI(inst7_O), .S(inst9_O6), .O(inst10_O));
XORCY inst11 (.LI(inst9_O6), .CI(inst7_O), .O(inst11_O));
LUT6_2 #(.INIT(64'h66666666AAAAAAAA)) inst12 (.I0(I0[4]), .I1(I1[4]), .I2(1'b0), .I3(1'b0), .I4(1'b0), .I5(1'b1), .O5(inst12_O5), .O6(inst12_O6));
MUXCY inst13 (.DI(inst12_O5), .CI(inst10_O), .S(inst12_O6), .O(inst13_O));
XORCY inst14 (.LI(inst12_O6), .CI(inst10_O), .O(inst14_O));
LUT6_2 #(.INIT(64'h66666666AAAAAAAA)) inst15 (.I0(I0[5]), .I1(I1[5]), .I2(1'b0), .I3(1'b0), .I4(1'b0), .I5(1'b1), .O5(inst15_O5), .O6(inst15_O6));
MUXCY inst16 (.DI(inst15_O5), .CI(inst13_O), .S(inst15_O6), .O(inst16_O));
XORCY inst17 (.LI(inst15_O6), .CI(inst13_O), .O(inst17_O));
LUT6_2 #(.INIT(64'h66666666AAAAAAAA)) inst18 (.I0(I0[6]), .I1(I1[6]), .I2(1'b0), .I3(1'b0), .I4(1'b0), .I5(1'b1), .O5(inst18_O5), .O6(inst18_O6));
MUXCY inst19 (.DI(inst18_O5), .CI(inst16_O), .S(inst18_O6), .O(inst19_O));
XORCY inst20 (.LI(inst18_O6), .CI(inst16_O), .O(inst20_O));
LUT6_2 #(.INIT(64'h66666666AAAAAAAA)) inst21 (.I0(I0[7]), .I1(I1[7]), .I2(1'b0), .I3(1'b0), .I4(1'b0), .I5(1'b1), .O5(inst21_O5), .O6(inst21_O6));
MUXCY inst22 (.DI(inst21_O5), .CI(inst19_O), .S(inst21_O6), .O(inst22_O));
XORCY inst23 (.LI(inst21_O6), .CI(inst19_O), .O(inst23_O));
assign O = {inst23_O,inst20_O,inst17_O,inst14_O,inst11_O,inst8_O,inst5_O,inst2_O};
assign COUT = inst22_O;
endmodule

module Mux2 (input [1:0] I, input  S, output  O);
wire  inst0_O;
LUT3 #(.INIT(8'hCA)) inst0 (.I0(I[0]), .I1(I[1]), .I2(S), .O(inst0_O));
assign O = inst0_O;
endmodule

module Mux2x8 (input [7:0] I0, input [7:0] I1, input  S, output [7:0] O);
wire  inst0_O;
wire  inst1_O;
wire  inst2_O;
wire  inst3_O;
wire  inst4_O;
wire  inst5_O;
wire  inst6_O;
wire  inst7_O;
Mux2 inst0 (.I({I1[0],I0[0]}), .S(S), .O(inst0_O));
Mux2 inst1 (.I({I1[1],I0[1]}), .S(S), .O(inst1_O));
Mux2 inst2 (.I({I1[2],I0[2]}), .S(S), .O(inst2_O));
Mux2 inst3 (.I({I1[3],I0[3]}), .S(S), .O(inst3_O));
Mux2 inst4 (.I({I1[4],I0[4]}), .S(S), .O(inst4_O));
Mux2 inst5 (.I({I1[5],I0[5]}), .S(S), .O(inst5_O));
Mux2 inst6 (.I({I1[6],I0[6]}), .S(S), .O(inst6_O));
Mux2 inst7 (.I({I1[7],I0[7]}), .S(S), .O(inst7_O));
assign O = {inst7_O,inst6_O,inst5_O,inst4_O,inst3_O,inst2_O,inst1_O,inst0_O};
endmodule

module Register8 (input [7:0] I, output [7:0] O, input  CLK);
wire  inst0_Q;
wire  inst1_Q;
wire  inst2_Q;
wire  inst3_Q;
wire  inst4_Q;
wire  inst5_Q;
wire  inst6_Q;
wire  inst7_Q;
FDRSE #(.INIT(1'h0)) inst0 (.C(CLK), .CE(1'b1), .R(1'b0), .S(1'b0), .D(I[0]), .Q(inst0_Q));
FDRSE #(.INIT(1'h0)) inst1 (.C(CLK), .CE(1'b1), .R(1'b0), .S(1'b0), .D(I[1]), .Q(inst1_Q));
FDRSE #(.INIT(1'h0)) inst2 (.C(CLK), .CE(1'b1), .R(1'b0), .S(1'b0), .D(I[2]), .Q(inst2_Q));
FDRSE #(.INIT(1'h0)) inst3 (.C(CLK), .CE(1'b1), .R(1'b0), .S(1'b0), .D(I[3]), .Q(inst3_Q));
FDRSE #(.INIT(1'h0)) inst4 (.C(CLK), .CE(1'b1), .R(1'b0), .S(1'b0), .D(I[4]), .Q(inst4_Q));
FDRSE #(.INIT(1'h0)) inst5 (.C(CLK), .CE(1'b1), .R(1'b0), .S(1'b0), .D(I[5]), .Q(inst5_Q));
FDRSE #(.INIT(1'h0)) inst6 (.C(CLK), .CE(1'b1), .R(1'b0), .S(1'b0), .D(I[6]), .Q(inst6_Q));
FDRSE #(.INIT(1'h0)) inst7 (.C(CLK), .CE(1'b1), .R(1'b0), .S(1'b0), .D(I[7]), .Q(inst7_Q));
assign O = {inst7_Q,inst6_Q,inst5_Q,inst4_Q,inst3_Q,inst2_Q,inst1_Q,inst0_Q};
endmodule

module CounterLoad8 (input [7:0] DATA, input  LOAD, output [7:0] O, output  COUT, input  CLK);
wire [7:0] inst0_O;
wire  inst0_COUT;
wire [7:0] inst1_O;
wire [7:0] inst2_O;
Add8_cout inst0 (.I0(inst2_O), .I1({1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b0,1'b1}), .O(inst0_O), .COUT(inst0_COUT));
Mux2x8 inst1 (.I0(inst0_O), .I1(DATA), .S(LOAD), .O(inst1_O));
Register8 inst2 (.I(inst1_O), .O(inst2_O), .CLK(CLK));
assign O = inst2_O;
assign COUT = inst0_COUT;
endmodule

