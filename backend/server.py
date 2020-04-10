from flask import Flask, request, jsonify
from flask_cors import CORS
from flask import request

app = Flask(__name__)
CORS(app)

@app.route("/")
def root():
    return "Root"

@app.route("/weapon_ranking")
def weapon_rankning():
    # Hard coded for now because the data is not changing
    weapon_names1 = ['WeapHK416_C', 'WeapHK416_C', 'WeapHK416_C', 'WeapHK416_C', 'WeapHK416_C', 'WeapHK416_C', 'WeapHK416_C', 'WeapHK416_C', 'WeapHK416_C']
    best_scopes1 = ['Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C']
    best_muzzle1 = ['Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C']
    kill_count1 = [109089, 206166, 157559, 138519, 117681, 86735, 58970, 25746, 840]
    weapon_names2 = ['WeapAK47_C', 'WeapFNFal_C', 'WeapFNFal_C', 'WeapFNFal_C', 'WeapFNFal_C', 'WeapFNFal_C', 'WeapFNFal_C', 'WeapAK47_C', 'WeapAK47_C']
    best_scopes2 = ['Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_Scope6x_C', 'Item_Attach_Weapon_Upper_Scope6x_C', 'Item_Attach_Weapon_Upper_Scope6x_C', 'Item_Attach_Weapon_Upper_Scope6x_C', 'Item_Attach_Weapon_Upper_Scope6x_C', 'Item_Attach_Weapon_Upper_Scope6x_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C']
    best_muzzle2 = ['Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Suppressor_Large_C', 'Item_Attach_Weapon_Muzzle_Suppressor_Large_C', 'Item_Attach_Weapon_Muzzle_Suppressor_Large_C', 'Item_Attach_Weapon_Muzzle_Suppressor_Large_C', 'Item_Attach_Weapon_Muzzle_Suppressor_SniperRifle_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C']
    kill_count2 = [85555, 73838, 65940, 71067, 71522, 53029, 23252, 5018, 209]
    weapon_names3 = ['WeapSCAR-L_C', 'WeapAK47_C', 'WeapAK47_C', 'WeapSKS_C', 'WeapSKS_C', 'WeapSKS_C', 'WeapAK47_C', 'WeapSCAR-L_C', 'WeapSCAR-L_C']
    kill_count3 = [70050, 66491, 40073, 35605, 33780, 23978, 11345, 3079, 124]
    best_scope3 = ['Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_Scope6x_C', 'Item_Attach_Weapon_Upper_Scope6x_C', 'Item_Attach_Weapon_Upper_Scope6x_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C', 'Item_Attach_Weapon_Upper_DotSight_01_C']
    best_muzzle3 = ['Item_Attach_Weapon_Muzzle_FlashHider_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Suppressor_Large_C', 'Item_Attach_Weapon_Muzzle_Suppressor_Large_C', 'Item_Attach_Weapon_Muzzle_Suppressor_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C', 'Item_Attach_Weapon_Muzzle_Compensator_Large_C']

    return jsonify(
        {
            "first": [
                {
                    "Weapon_name": name,
                    "Scope": scope,
                    "Muzzle": muzzle,
                    "Kill_Count": kill
                }
                for name, scope, muzzle, kill in zip(weapon_names1, best_scopes1, best_muzzle1, kill_count1)
            ],
            "second": [
                {
                    "Weapon_name": name,
                    "Scope": scope,
                    "Muzzle": muzzle,
                    "Kill_Count": kill
                }
                for name, scope, muzzle, kill in zip(weapon_names2, best_scopes2, best_muzzle2, kill_count2)
            ],
            "third": [
                {
                    "Weapon_name": name,
                    "Scope": scope,
                    "Muzzle": muzzle,
                    "Kill_Count": kill
                }
                for name, scope, muzzle, kill in zip(weapon_names3, best_scope3, best_muzzle3, kill_count3)
            ]
        }
    )


@app.route("/kill")
def get_kill_loc():
    return "TODO"

if __name__ == '__main__':
    app.run(host='master', port=12315)
