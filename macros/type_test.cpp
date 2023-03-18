#include <TFile.h>
#include <TTree.h>
#include <typeinfo>

void type_test() {
  TFile* mfile = TFile::Open("new100.root");

  TTree* mtree = (TTree*)mfile->Get("h1");

  Float_t mvalue;
  mtree->SetBranchAddress("X_vtx", &mvalue);

  mtree->GetEntry(0);
  
  printf("Type name of the first value in branch X_vtx: %f %s\n", mvalue, typeid(mvalue).name());

  mfile->Close();

  TFile* file = TFile::Open("../batch/data/AnaBarMC_Gen_7001.root");

  TTree* tree = (TTree*)file->Get("h1");

  Float_t value;
  tree->SetBranchAddress("X_vtx", &value);

  tree->GetEntry(0);
  
  printf("Type name of the first value in branch X_vtx: %f %s\n", value, typeid(value).name());

  file->Close();
}

