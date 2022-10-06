/* Created by Language version: 7.7.0 */
/* VECTORIZED */
#define NRN_VECTORIZED 1
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "mech_api.h"
#undef PI
#define nil 0
#include "md1redef.h"
#include "section.h"
#include "nrniv_mf.h"
#include "md2redef.h"
 
#if METHOD3
extern int _method3;
#endif

#if !NRNGPU
#undef exp
#define exp hoc_Exp
extern double hoc_Exp(double);
#endif
 
#define nrn_init _nrn_init__Pyr
#define _nrn_initial _nrn_initial__Pyr
#define nrn_cur _nrn_cur__Pyr
#define _nrn_current _nrn_current__Pyr
#define nrn_jacob _nrn_jacob__Pyr
#define nrn_state _nrn_state__Pyr
#define _net_receive _net_receive__Pyr 
#define states states__Pyr 
 
#define _threadargscomma_ _p, _ppvar, _thread, _nt,
#define _threadargsprotocomma_ double* _p, Datum* _ppvar, Datum* _thread, NrnThread* _nt,
#define _threadargs_ _p, _ppvar, _thread, _nt
#define _threadargsproto_ double* _p, Datum* _ppvar, Datum* _thread, NrnThread* _nt
 	/*SUPPRESS 761*/
	/*SUPPRESS 762*/
	/*SUPPRESS 763*/
	/*SUPPRESS 765*/
	 extern double *getarg();
 /* Thread safe. No static _p or _ppvar. */
 
#define t _nt->_t
#define dt _nt->_dt
#define v_init _p[0]
#define v_init_columnindex 0
#define vr _p[1]
#define vr_columnindex 1
#define vt _p[2]
#define vt_columnindex 2
#define c _p[3]
#define c_columnindex 3
#define vpeak _p[4]
#define vpeak_columnindex 4
#define Cm _p[5]
#define Cm_columnindex 5
#define a _p[6]
#define a_columnindex 6
#define b _p[7]
#define b_columnindex 7
#define d _p[8]
#define d_columnindex 8
#define khigh _p[9]
#define khigh_columnindex 9
#define klow _p[10]
#define klow_columnindex 10
#define Ishift _p[11]
#define Ishift_columnindex 11
#define Iinj _p[12]
#define Iinj_columnindex 12
#define stim_start _p[13]
#define stim_start_columnindex 13
#define stim_stop _p[14]
#define stim_stop_columnindex 14
#define k _p[15]
#define k_columnindex 15
#define Iext _p[16]
#define Iext_columnindex 16
#define vm _p[17]
#define vm_columnindex 17
#define um _p[18]
#define um_columnindex 18
#define Dvm _p[19]
#define Dvm_columnindex 19
#define Dum _p[20]
#define Dum_columnindex 20
#define v _p[21]
#define v_columnindex 21
#define _g _p[22]
#define _g_columnindex 22
#define _nd_area  *_ppvar[0]._pval
 
#if MAC
#if !defined(v)
#define v _mlhv
#endif
#if !defined(h)
#define h _mlhh
#endif
#endif
 
#if defined(__cplusplus)
extern "C" {
#endif
 static int hoc_nrnpointerindex =  -1;
 static Datum* _extcall_thread;
 static Prop* _extcall_prop;
 /* external NEURON variables */
 /* declaration of user functions */
 static int _mechtype;
extern void _nrn_cacheloop_reg(int, int);
extern void hoc_register_prop_size(int, int, int);
extern void hoc_register_limits(int, HocParmLimits*);
extern void hoc_register_units(int, HocParmUnits*);
extern void nrn_promote(Prop*, int, int);
extern Memb_func* memb_func;
 
#define NMODL_TEXT 1
#if NMODL_TEXT
static const char* nmodl_file_text;
static const char* nmodl_filename;
extern void hoc_reg_nmodl_text(int, const char*);
extern void hoc_reg_nmodl_filename(int, const char*);
#endif

 extern Prop* nrn_point_prop_;
 static int _pointtype;
 static void* _hoc_create_pnt(Object* _ho) { void* create_point_process(int, Object*);
 return create_point_process(_pointtype, _ho);
}
 static void _hoc_destroy_pnt(void*);
 static double _hoc_loc_pnt(void* _vptr) {double loc_point_process(int, void*);
 return loc_point_process(_pointtype, _vptr);
}
 static double _hoc_has_loc(void* _vptr) {double has_loc_point(void*);
 return has_loc_point(_vptr);
}
 static double _hoc_get_loc_pnt(void* _vptr) {
 double get_loc_point_process(void*); return (get_loc_point_process(_vptr));
}
 extern void _nrn_setdata_reg(int, void(*)(Prop*));
 static void _setdata(Prop* _prop) {
 _extcall_prop = _prop;
 }
 static void _hoc_setdata(void* _vptr) { Prop* _prop;
 _prop = ((Point_process*)_vptr)->_prop;
   _setdata(_prop);
 }
 /* connect user functions to hoc names */
 static VoidFunc hoc_intfunc[] = {
 0,0
};
 static Member_func _member_func[] = {
 "loc", _hoc_loc_pnt,
 "has_loc", _hoc_has_loc,
 "get_loc", _hoc_get_loc_pnt,
 0, 0
};
 /* declare global and static user variables */
 /* some parameters have upper and lower limits */
 static HocParmLimits _hoc_parm_limits[] = {
 0,0,0
};
 static HocParmUnits _hoc_parm_units[] = {
 "v_init", "mV",
 "vr", "mV",
 "vt", "mV",
 "c", "mV",
 "vpeak", "mV",
 "Cm", "pF",
 "a", "1/ms",
 "b", "nS",
 "d", "pA",
 "khigh", "nS/mV",
 "klow", "nS/mV",
 "Ishift", "pA",
 "Iinj", "pA",
 "stim_start", "ms",
 "stim_stop", "ms",
 "vm", "mV",
 "um", "pA",
 "k", "nS/mV",
 "Iext", "nA",
 0,0
};
 static double delta_t = 0.01;
 static double um0 = 0;
 static double vm0 = 0;
 /* connect global user variables to hoc */
 static DoubScal hoc_scdoub[] = {
 0,0
};
 static DoubVec hoc_vdoub[] = {
 0,0,0
};
 static double _sav_indep;
 static void nrn_alloc(Prop*);
static void  nrn_init(NrnThread*, _Memb_list*, int);
static void nrn_state(NrnThread*, _Memb_list*, int);
 static void nrn_cur(NrnThread*, _Memb_list*, int);
static void  nrn_jacob(NrnThread*, _Memb_list*, int);
 static void _hoc_destroy_pnt(void* _vptr) {
   destroy_point_process(_vptr);
}
 
static int _ode_count(int);
static void _ode_map(int, double**, double**, double*, Datum*, double*, int);
static void _ode_spec(NrnThread*, _Memb_list*, int);
static void _ode_matsol(NrnThread*, _Memb_list*, int);
 
#define _cvode_ieq _ppvar[2]._i
 static void _ode_matsol_instance1(_threadargsproto_);
 /* connect range variables in _p that hoc is supposed to know about */
 static const char *_mechanism[] = {
 "7.7.0",
"Pyr",
 "v_init",
 "vr",
 "vt",
 "c",
 "vpeak",
 "Cm",
 "a",
 "b",
 "d",
 "khigh",
 "klow",
 "Ishift",
 "Iinj",
 "stim_start",
 "stim_stop",
 0,
 "k",
 "Iext",
 0,
 "vm",
 "um",
 0,
 0};
 
extern Prop* need_memb(Symbol*);

static void nrn_alloc(Prop* _prop) {
	Prop *prop_ion;
	double *_p; Datum *_ppvar;
  if (nrn_point_prop_) {
	_prop->_alloc_seq = nrn_point_prop_->_alloc_seq;
	_p = nrn_point_prop_->param;
	_ppvar = nrn_point_prop_->dparam;
 }else{
 	_p = nrn_prop_data_alloc(_mechtype, 23, _prop);
 	/*initialize range parameters*/
 	v_init = -65;
 	vr = -61.8;
 	vt = -57;
 	c = -65.8;
 	vpeak = 22.6;
 	Cm = 115;
 	a = 0.0012;
 	b = 3;
 	d = 10;
 	khigh = 3.3;
 	klow = 0.1;
 	Ishift = 0;
 	Iinj = 100;
 	stim_start = 0;
 	stim_stop = 1000;
  }
 	_prop->param = _p;
 	_prop->param_size = 23;
  if (!nrn_point_prop_) {
 	_ppvar = nrn_prop_datum_alloc(_mechtype, 3, _prop);
  }
 	_prop->dparam = _ppvar;
 	/*connect ionic variables to this model*/
 
}
 static void _initlists();
  /* some states have an absolute tolerance */
 static Symbol** _atollist;
 static HocStateTolerance _hoc_state_tol[] = {
 0,0
};
 static void _thread_mem_init(Datum*);
 static void _thread_cleanup(Datum*);
 extern Symbol* hoc_lookup(const char*);
extern void _nrn_thread_reg(int, int, void(*)(Datum*));
extern void _nrn_thread_table_reg(int, void(*)(double*, Datum*, Datum*, NrnThread*, int));
extern void hoc_register_tolerance(int, HocStateTolerance*, Symbol***);
extern void _cvode_abstol( Symbol**, double*, int);

 void _Pyr_reg() {
	int _vectorized = 1;
  _initlists();
 	_pointtype = point_register_mech(_mechanism,
	 nrn_alloc,nrn_cur, nrn_jacob, nrn_state, nrn_init,
	 hoc_nrnpointerindex, 5,
	 _hoc_create_pnt, _hoc_destroy_pnt, _member_func);
  _extcall_thread = (Datum*)ecalloc(4, sizeof(Datum));
  _thread_mem_init(_extcall_thread);
 _mechtype = nrn_get_mechtype(_mechanism[1]);
     _nrn_setdata_reg(_mechtype, _setdata);
     _nrn_thread_reg(_mechtype, 1, _thread_mem_init);
     _nrn_thread_reg(_mechtype, 0, _thread_cleanup);
 #if NMODL_TEXT
  hoc_reg_nmodl_text(_mechtype, nmodl_file_text);
  hoc_reg_nmodl_filename(_mechtype, nmodl_filename);
#endif
  hoc_register_prop_size(_mechtype, 23, 3);
  hoc_register_dparam_semantics(_mechtype, 0, "area");
  hoc_register_dparam_semantics(_mechtype, 1, "pntproc");
  hoc_register_dparam_semantics(_mechtype, 2, "cvodeieq");
 	hoc_register_cvode(_mechtype, _ode_count, _ode_map, _ode_spec, _ode_matsol);
 	hoc_register_tolerance(_mechtype, _hoc_state_tol, &_atollist);
 	hoc_register_var(hoc_scdoub, hoc_vdoub, hoc_intfunc);
 	ivoc_help("help ?1 Pyr /home/shailesh/Work/Ferguson2014/Neuron/Pyr.mod\n");
 hoc_register_limits(_mechtype, _hoc_parm_limits);
 hoc_register_units(_mechtype, _hoc_parm_units);
 }
static int _reset;
static char *modelname = "CA1 Pyr model";

static int error;
static int _ninits = 0;
static int _match_recurse=1;
static void _modl_cleanup(){ _match_recurse=1;}
 
#define _deriv1_advance _thread[0]._i
#define _dith1 1
#define _recurse _thread[2]._i
#define _newtonspace1 _thread[3]._pvoid
 
static int _ode_spec1(_threadargsproto_);
/*static int _ode_matsol1(_threadargsproto_);*/
 static int _slist2[2];
  static int _slist1[2], _dlist1[2];
 static int states(_threadargsproto_);
 
/*CVODE*/
 static int _ode_spec1 (double* _p, Datum* _ppvar, Datum* _thread, NrnThread* _nt) {int _reset = 0; {
   Dum = a * ( b * ( vm - vr ) - um ) ;
   Dvm = ( k * ( vm - vr ) * ( vm - vt ) + Ishift + Iext - um ) / Cm ;
   }
 return _reset;
}
 static int _ode_matsol1 (double* _p, Datum* _ppvar, Datum* _thread, NrnThread* _nt) {
 Dum = Dum  / (1. - dt*( ( a )*( ( ( - 1.0 ) ) ) )) ;
 Dvm = Dvm  / (1. - dt*( ( ( (( ( k )*( ( 1.0 ) ) )*( ( vm - vt ) ) + ( k * ( vm - vr ) )*( ( 1.0 ) )) ) ) / Cm )) ;
  return 0;
}
 /*END CVODE*/
 
static int states (double* _p, Datum* _ppvar, Datum* _thread, NrnThread* _nt) {int _reset=0; int error = 0;
 { double* _savstate1 = _thread[_dith1]._pval;
 double* _dlist2 = _thread[_dith1]._pval + 2;
 int _counte = -1;
 if (!_recurse) {
 _recurse = 1;
 {int _id; for(_id=0; _id < 2; _id++) { _savstate1[_id] = _p[_slist1[_id]];}}
 error = nrn_newton_thread(_newtonspace1, 2,_slist2, _p, states, _dlist2, _ppvar, _thread, _nt);
 _recurse = 0; if(error) {abort_run(error);}}
 {
   Dum = a * ( b * ( vm - vr ) - um ) ;
   Dvm = ( k * ( vm - vr ) * ( vm - vt ) + Ishift + Iext - um ) / Cm ;
   {int _id; for(_id=0; _id < 2; _id++) {
if (_deriv1_advance) {
 _dlist2[++_counte] = _p[_dlist1[_id]] - (_p[_slist1[_id]] - _savstate1[_id])/dt;
 }else{
_dlist2[++_counte] = _p[_slist1[_id]] - _savstate1[_id];}}}
 } }
 return _reset;}
 
static int _ode_count(int _type){ return 2;}
 
static void _ode_spec(NrnThread* _nt, _Memb_list* _ml, int _type) {
   double* _p; Datum* _ppvar; Datum* _thread;
   Node* _nd; double _v; int _iml, _cntml;
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _nd = _ml->_nodelist[_iml];
    v = NODEV(_nd);
     _ode_spec1 (_p, _ppvar, _thread, _nt);
 }}
 
static void _ode_map(int _ieq, double** _pv, double** _pvdot, double* _pp, Datum* _ppd, double* _atol, int _type) { 
	double* _p; Datum* _ppvar;
 	int _i; _p = _pp; _ppvar = _ppd;
	_cvode_ieq = _ieq;
	for (_i=0; _i < 2; ++_i) {
		_pv[_i] = _pp + _slist1[_i];  _pvdot[_i] = _pp + _dlist1[_i];
		_cvode_abstol(_atollist, _atol, _i);
	}
 }
 
static void _ode_matsol_instance1(_threadargsproto_) {
 _ode_matsol1 (_p, _ppvar, _thread, _nt);
 }
 
static void _ode_matsol(NrnThread* _nt, _Memb_list* _ml, int _type) {
   double* _p; Datum* _ppvar; Datum* _thread;
   Node* _nd; double _v; int _iml, _cntml;
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _nd = _ml->_nodelist[_iml];
    v = NODEV(_nd);
 _ode_matsol_instance1(_threadargs_);
 }}
 
static void _thread_mem_init(Datum* _thread) {
   _thread[_dith1]._pval = (double*)ecalloc(4, sizeof(double));
   _newtonspace1 = nrn_cons_newtonspace(2);
 }
 
static void _thread_cleanup(Datum* _thread) {
   free((void*)(_thread[_dith1]._pval));
   nrn_destroy_newtonspace(_newtonspace1);
 }

static void initmodel(double* _p, Datum* _ppvar, Datum* _thread, NrnThread* _nt) {
  int _i; double _save;{
  um = um0;
  vm = vm0;
 {
   vm = v_init ;
   um = 0.0 ;
   }
 
}
}

static void nrn_init(NrnThread* _nt, _Memb_list* _ml, int _type){
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; double _v; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 v = _v;
 initmodel(_p, _ppvar, _thread, _nt);
}
}

static double _nrn_current(double* _p, Datum* _ppvar, Datum* _thread, NrnThread* _nt, double _v){double _current=0.;v=_v;{
} return _current;
}

static void nrn_cur(NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; int* _ni; double _rhs, _v; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 
}
 
}

static void nrn_jacob(NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml];
#if CACHEVEC
  if (use_cachevec) {
	VEC_D(_ni[_iml]) += _g;
  }else
#endif
  {
     _nd = _ml->_nodelist[_iml];
	NODED(_nd) += _g;
  }
 
}
 
}

static void nrn_state(NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; double _v = 0.0; int* _ni; int _iml, _cntml;
double _dtsav = dt;
if (secondorder) { dt *= 0.5; }
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
 _nd = _ml->_nodelist[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 v=_v;
{
 {  _deriv1_advance = 1;
 derivimplicit_thread(2, _slist1, _dlist1, _p, states, _ppvar, _thread, _nt);
_deriv1_advance = 0;
     if (secondorder) {
    int _i;
    for (_i = 0; _i < 2; ++_i) {
      _p[_slist1[_i]] += dt*_p[_dlist1[_i]];
    }}
 } {
   if ( vm > vpeak ) {
     vm = c ;
     um = um + d ;
     }
   if ( vm < vt ) {
     k = klow ;
     }
   else {
     k = khigh ;
     }
   if ( ( t >= stim_start )  && ( t < stim_stop ) ) {
     Iext = Iinj ;
     }
   else {
     Iext = 0.0 ;
     }
   }
}}
 dt = _dtsav;
}

static void terminal(){}

static void _initlists(){
 double _x; double* _p = &_x;
 int _i; static int _first = 1;
  if (!_first) return;
 _slist1[0] = um_columnindex;  _dlist1[0] = Dum_columnindex;
 _slist1[1] = vm_columnindex;  _dlist1[1] = Dvm_columnindex;
 _slist2[0] = um_columnindex;
 _slist2[1] = vm_columnindex;
_first = 0;
}

#if defined(__cplusplus)
} /* extern "C" */
#endif

#if NMODL_TEXT
static const char* nmodl_filename = "/home/shailesh/Work/Ferguson2014/Neuron/Pyr.mod";
static const char* nmodl_file_text = 
  "TITLE CA1 Pyr model\n"
  ": NMODL implementation of CA1 PYR model\n"
  ": Implemented by: Shailesh Appukuttan (CNRS), August 2022\n"
  ": \n"
  ": Original work: \n"
  ": Ferguson KA, Huh CY, Amilhon B, Williams S, Skinner FK (2014)\n"
  ": Simple, biologically-constrained CA1 pyramidal cell models \n"
  ": using an intact, whole hippocampus context . \n"
  ": F1000Research 2015, 3:104 (https://doi.org/10.12688/f1000research.3894.2) \n"
  "\n"
  "NEURON {\n"
  "    POINT_PROCESS Pyr\n"
  "    RANGE v_init, vr, vt, c, vpeak, Cm, a, b, d, khigh, klow, Ishift, Iinj, Iext, stim_start, stim_stop, k\n"
  "}\n"
  "\n"
  "UNITS {\n"
  "    (mV) = (millivolt)\n"
  "    (pA) = (picoamp)\n"
  "    (nS) = (nanosiemens)\n"
  "}\n"
  "\n"
  "INITIAL {\n"
  "    vm = v_init\n"
  "    um = 0\n"
  "}\n"
  "\n"
  "PARAMETER {\n"
  "    : Default values correspond to strongly adapting model\n"
  "    v_init = -65 (mV)\n"
  "    vr = -61.8 (mV)\n"
  "    vt = -57.0 (mV)\n"
  "    c = -65.8 (mV)\n"
  "    vpeak = 22.6 (mV)\n"
  "    Cm = 115  (pF)\n"
  "    a = 0.0012 (1/ms)\n"
  "    b = 3 (nS)\n"
  "    d = 10 (pA)\n"
  "    khigh = 3.3  (nS/mV)\n"
  "    klow = 0.1 (nS/mV)\n"
  "\n"
  "    Ishift = 0 (pA)\n"
  "    Iinj = 100 (pA)\n"
  "    stim_start = 0.0 (ms)\n"
  "    stim_stop = 1000.0 (ms)\n"
  "}\n"
  "\n"
  "ASSIGNED {\n"
  "    k (nS/mV)\n"
  "    Iext (nA)\n"
  "}\n"
  "\n"
  "STATE {\n"
  "    vm (mV)\n"
  "    um (pA)\n"
  "}\n"
  "\n"
  "BREAKPOINT {\n"
  "    if (vm > vpeak) {\n"
  "        vm = c\n"
  "        um = um + d\n"
  "    }\n"
  "\n"
  "    if (vm<vt) {\n"
  "        k = klow\n"
  "    } else {\n"
  "        k = khigh\n"
  "    }\n"
  "\n"
  "    if ((t >= stim_start) && (t <stim_stop)) {\n"
  "        Iext = Iinj\n"
  "    } else {\n"
  "        Iext = 0\n"
  "    }\n"
  "\n"
  "    SOLVE states METHOD derivimplicit\n"
  "}\n"
  "\n"
  "DERIVATIVE states {\n"
  "    um' = a*(b*(vm-vr)-um)\n"
  "    vm' = (k*(vm-vr)*(vm-vt)+Ishift+Iext -um)/Cm\n"
  "}\n"
  ;
#endif
