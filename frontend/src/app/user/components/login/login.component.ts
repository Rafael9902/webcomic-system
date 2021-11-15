import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup} from "@angular/forms";
import { AuthService} from "../../../auth/auth.service";
import { Router } from '@angular/router';
import * as utils  from "../../../shared/utils";


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  register: boolean = false;

  credentialsForm = new FormGroup({
    email: new FormControl(''),
    password: new FormControl('')
  });

  constructor(private _authService: AuthService, private _router: Router) {}

  ngOnInit(): void {
    if(!this._authService.isLoggedIn())
      this._router.navigate(["/home"]);

    this.validateRegisterUser()
  }

  validateRegisterUser(){
    if(localStorage.getItem("register")){
      this.register = true;
      localStorage.clear();
    }

  }

  onSubmit(){
    this._authService.login(this.credentialsForm.value).subscribe({
      next(response){
        console.log(response);
        if(response.status == 200)
          utils.saveSessionToken(response.token);
      },
      error(msg){
        console.error(msg);
      }
    });

    this.ngOnInit();
  }

}
