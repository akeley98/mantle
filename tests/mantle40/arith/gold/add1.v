module Add1 (input [0:0] I0, input [0:0] I1, output [0:0] O, output  COUT);
wire  inst0_O;
wire  inst1_CO;
SB_LUT4 #(.LUT_INIT(16'hC33C)) inst0 (.I0(1'b0), .I1(I0[0]), .I2(I1[0]), .I3(1'b0), .O(inst0_O));
SB_CARRY inst1 (.I0(I0[0]), .I1(I1[0]), .CI(1'b0), .CO(inst1_CO));
assign O = {inst0_O};
assign COUT = inst1_CO;
endmodule

module main (input  A0, input  B0, output  D2, output  D1, input  CLKIN);
wire [0:0] inst0_O;
wire  inst0_COUT;
Add1 inst0 (.I0({A0}), .I1({B0}), .O(inst0_O), .COUT(inst0_COUT));
assign D2 = inst0_COUT;
assign D1 = inst0_O[0];
endmodule
